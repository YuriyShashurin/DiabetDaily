from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=150, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(label='Имя', max_length=150)
    last_name = forms.CharField(label='Имя', max_length=150)
    email = forms.EmailField(required=True, max_length=150)
