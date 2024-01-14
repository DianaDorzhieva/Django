from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms
from django.contrib.auth import get_user_model

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("пароли не совпадают")
        return cd['password1']

    # def clean_email(self):
    #     email = self.cleaned_data
    #     if get_user_model().objects.filter(email=email).exists():
    #         raise forms.ValidationError("Такой email уже существует")
    #     return email


class UserForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'avatar', 'phone', 'county')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
