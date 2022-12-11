from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, FormView, CreateView, ListView
from django_resized import ResizedImageField

from app1.forms import RegisterForm, LoginForm, EditProfileForm
from app1.models import Category, Post, User, Comment, About


class MainView(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_post'] = Post.objects.filter(is_publish=Post.Status.ACTIVE).order_by('created_at').last()
        context['posts'] = Post.objects.filter(is_publish=Post.Status.ACTIVE).order_by('-created_at').all()[1:]
        context['future_posts'] = Post.objects.order_by('-created_at')[:3]
        context['categories'] = Category.objects.all()
        return context


class BlogView(TemplateView):
    template_name = 'app1/blog-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all()
        context['future_posts'] = Post.objects.order_by('-created_at')[:3]
        return context


class ContactView(TemplateView):
    template_name = 'app1/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future_posts'] = Post.objects.order_by('-created_at')[:3]
        return context


class PostView(TemplateView):
    template_name = 'app1/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.filter(slug=self.request.path.split('/')[-1]).first()
        context['author'] = User.objects.all().first()
        context['bio'] = User.objects.all().first()
        context['future_posts'] = Post.objects.order_by('-created_at')[:3]
        context['comments'] = Comment.objects.filter(post=context['post'])
        return context


class AboutView(TemplateView):
    template_name = 'app1/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['future_posts'] = Post.objects.order_by('-created_at')[:3]
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


class CustomAbout(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context


class ProfileView(FormView):
    template_name = 'app1/profile.html'
    form_class = EditProfileForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['future_posts'] = Post.objects.order_by('-created_at')[:3]
        return context

