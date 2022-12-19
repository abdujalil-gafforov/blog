from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from app1.models import User, Post, Category


class ChangePasswordForm(Form):
    password = CharField(max_length=255)
    new_password = CharField(max_length=255)
    confirm_password = CharField(max_length=255)

    class Meta:
        fields = ('cur_password', 'new_password', 'con_password')


class EditProfileForm(UserChangeForm):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'bio', 'phone_number', 'gender', 'photo')
        model = User


class LoginForm(AuthenticationForm):

    def clean_password(self):
        username = self.data.get('username')
        password = self.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and not user.check_password(password):
            raise ValidationError('ERROR')
        return password

    class Meta:
        fields = ('username', 'password')
        model = User


class RegisterForm(ModelForm):

    def clean(self):
        data = super().clean()
        data['password'] = make_password(data['password'])
        return data

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        model = User


class CreatePostForm(ModelForm):
    category = ModelMultipleChoiceField(
        queryset=Category.objects.order_by('name'),
        label='Category',
        widget=CheckboxSelectMultiple
    )
    class Meta:
        fields = ('title', 'image', 'category', 'body')
        model = Post
