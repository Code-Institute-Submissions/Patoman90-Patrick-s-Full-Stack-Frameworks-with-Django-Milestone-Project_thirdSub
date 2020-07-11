from django import forms
from .models import quote
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

"""
Form for logging a user in.
"""


class UserLoginForm(forms.Form):
    username = forms.CharField()
    user_password = forms.CharField(widget=forms.PasswordInput)


"""
Form for registering a user.
"""


class MakeUserAccount(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2


""" User quote form """


class UserQuoteForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    user_quote = forms.CharField(max_length=500)
    phone_number = forms.CharField(max_length=20)
    date = forms.DateField()
