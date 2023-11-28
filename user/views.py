from django.shortcuts import redirect, render

from user import forms, models
from util.util import BaseView


class Create(BaseView):
    template_name = "user/create.html"

    def get(self, request, *args, **kwargs):
        return self.render(kwargs, form=forms.UserRegisterForm())

    def post(self, request, **kwargs):
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            model = models.AppUser()

            model.password = form.cleaned_data["password"]
            model.username = form.cleaned_data["username"]
            model.save()
            return redirect('mcwall:index')
        return self.render(kwargs, form=form)
