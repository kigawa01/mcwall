from django.shortcuts import redirect

from user import forms, models
from util.util import BaseView, Hash


class Create(BaseView):
    template_name = "user/create.html"

    def get(self, request, *args, **kwargs):
        return self.render(kwargs, form=forms.UserRegisterForm())

    def post(self, request, **kwargs):
        form = forms.UserRegisterForm(request.POST)
        if not form.is_valid():
            return self.render(kwargs, form=form)

        username = form.cleaned_data["username"]
        if models.AppUser.objects.filter(username=username).count() != 0:
            form.errors["username"] = f"'{username}'はすでに使用されています"
            return self.render(kwargs, form=form)

        model = models.AppUser()
        model.password = Hash.hash(form.cleaned_data["password"])
        model.username = username
        model.save()
        return redirect('mcwall:index')


class Login(BaseView):
    template_name = "user/login.html"
