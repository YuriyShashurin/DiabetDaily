from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class SignupForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=150, required=True)
    password = forms.CharField(label='Введить пароль', widget=forms.PasswordInput(), required=True)
    check_password = forms.CharField(label='Введите пароль повторно', widget=forms.PasswordInput(), required=True)
    first_name = forms.CharField(label='Имя', max_length=150)
    last_name = forms.CharField(label='Фамилия', max_length=150)
    email = forms.EmailField(required=True, max_length=150)
