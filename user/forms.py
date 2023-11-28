import django.forms


class UserRegisterForm(django.forms.Form):
    password = django.forms.CharField(max_length=128, required=True, min_length=8, widget=django.forms.PasswordInput)
    username = django.forms.CharField(max_length=150, required=True)
