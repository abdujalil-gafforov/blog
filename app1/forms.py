from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from app1.models import User


class EditProfileForm(UserChangeForm):

    # def clean(self):
    #     data = super().clean()
    #     return data

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'bio', 'email', 'phone_number', 'gender', 'photo')
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
