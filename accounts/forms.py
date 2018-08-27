from django.contrib.auth.models import User    # This gives the generic user class
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# User Registration Area
class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}), label="", min_length=4, max_length=150)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your email'}), label="", max_length=254, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}), label="", min_length=8, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label="", required=True)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )

        if commit:
            user.save()

            return user


# User Login Area
class UserLoginForm(AuthenticationForm):
    widgets = {
        'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
    }

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")

            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password entered')

            if not user.is_active:
                raise forms.ValidationError('This user is inactive')

            # This will return whatever is the default

            return super(UserLoginForm, self).cleaned(*args, **kwargs)