from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views import View

from user import forms, models
from util.util import BaseView


class Register(BaseView):
    template_name = "user/register.html"

    def get(self, request):
        return self.render(form=forms.UserRegisterForm())

    def post(self, request, ):
        form = forms.UserRegisterForm(request.POST)
        if not form.is_valid():
            return self.render(form=form)

        username = form.cleaned_data["username"]
        if models.AppUser.objects.filter(username=username).count() != 0:
            form.errors["username"] = f"'{username}'はすでに使用されています"
            return self.render(form=form)

        user = models.AppUser()
        user.set_password(form.cleaned_data["password"])
        user.username = username
        user.save()
        login(request, user)

        return redirect('mcwall:index')


class Login(BaseView):
    template_name = "user/login.html"

    def get(self, request, ):
        return self.render(form=forms.UserLoginForm())

    def post(self, request, **kwargs):
        form = forms.UserLoginForm(request.POST)
        if not form.is_valid():
            return self.render(form=form)

        user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user is None:
            form.errors["form"] = "ログインできませんでした"
            return self.render(form=form)
        login(request, user)

        return redirect('mcwall:index')


# noinspection PyMethodMayBeStatic
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("mcwall:index")
