from django.contrib.auth.views import LogoutView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from app1.views import MainView, BlogView, AboutView, ContactView, PostView, Login, RegisterView, ProfileView, \
    CreatePostView, ChangePasswordView, GeneratePdf, activate, test, ResetPasswordView

urlpatterns = [
    path('', MainView.as_view(), name='main_view'),
    path('blog', BlogView.as_view(), name='blog_view'),
    path('about', AboutView.as_view(), name='about_view'),
    path('contact', ContactView.as_view(), name='contact_view'),
    path('signup', RegisterView.as_view(), name='signup_view'),
    path('login', Login.as_view(), name='login_view'),
    path('profile', ProfileView.as_view(), name='profile_view'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('createpost', CreatePostView.as_view(), name='createpost_view'),
    path('logout', LogoutView.as_view(next_page='login_view'), name='logout'),
    path('post/<str:slug>', PostView.as_view(), name='post_view'),
    path('pdf/<str:slug>', GeneratePdf.as_view(), name='pdf'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='app1/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='app1/password_reset_complete.html'),
         name='password_reset_complete'),
    path('test', test, name='test'),

]
