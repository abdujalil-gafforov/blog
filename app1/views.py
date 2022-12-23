from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from app1.forms import RegisterForm, LoginForm, EditProfileForm, CreatePostForm, ChangePasswordForm
from app1.models import Category, Post, User, Comment, About
from app1.utils.html_to_pdf import render_to_pdf
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'app1/reset_password.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = HttpResponse('main_view')


class MyPosts(TemplateView):
    template_name = 'app1/my_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myposts'] = Post.objects.filter(user=self.request.user.pk)
        return context


class MainView(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(is_publish=Post.Status.ACTIVE).order_by('-created_at')
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        context['categories'] = Category.objects.all()
        return context


class BlogView(TemplateView):
    template_name = 'app1/blog-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        return context


class ContactView(TemplateView):
    template_name = 'app1/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        return context


class PostView(TemplateView):
    template_name = 'app1/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.filter(slug=self.request.path.split('/')[-1]).first()
        context['author'] = User.objects.all().first()
        context['bio'] = User.objects.all().first()
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        context['comments'] = Comment.objects.filter(post=context['post'])
        return context


class AboutView(TemplateView):
    template_name = 'app1/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'app1/new_post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('main_view')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user

        post.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class Login(LoginView):
    template_name = 'app1/login.html'
    form_class = LoginForm
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('main_view')


class RegisterView(CreateView):
    template_name = 'app1/signup.html'
    form_class = RegisterForm
    success_url = 'login'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()
        ActivateEmail(self.request, user, user.email)
        return super().form_valid(form)


class CustomAbout(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'app1/profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('profile_view')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['latest_posts'] = Post.objects.order_by('-created_at')[:3]
        return context

    def get_object(self, queryset=None):
        return self.request.user


class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = 'app1/profile.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        if check_password(form.cleaned_data['password'], self.request.user.password):
            if form.cleaned_data['new_password'] == form.cleaned_data['confirm_password']:
                user = self.request.user
                name = user.username
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                user = User.objects.get(username=name)
                if user:
                    login(self.request, user)
                    return render(self.request, self.template_name,
                                  {'error': 'Password Successfully changed', 'color': 'green'})
            else:
                return render(self.request, self.template_name,
                              {'error': 'Confirm Password is incorrect', 'color': 'red'})
        else:
            return render(self.request, self.template_name, {'error': 'Current Password is incorrect', 'color': 'red'})
        return super().form_valid(form)


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        data = {
            'post': Post.objects.get(slug=slug),
            'request': request,
        }
        pdf = render_to_pdf('html_to_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def ActivateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('activate_acc_email_msg.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    user1 = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user1.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user1.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('login_view')
    else:
        messages.error(request, 'Activation link is invalid!')

    return redirect('main_view')


def test(request):
    user = User.objects.get(username='pepe')
    ActivateEmail(request, user, user.email)
    return redirect('main_view')
