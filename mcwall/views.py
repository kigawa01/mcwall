import uuid

from django.urls import reverse_lazy
from django.views import generic

from mcwall import models, forms
from mcwall.models import ImageModel
from util.util import BaseView


# Create your views here.

class Index(generic.ListView):
    template_name = "mcwall/index.html"
    model = models.ImageModel
    ordering = "-created_at"
    paginate_by = 12


class Create(generic.CreateView):
    template_name = "mcwall/create.html"
    form_class = forms.ImageForm
    model = models.ImageModel
    success_url = reverse_lazy("mcwall:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Detail(BaseView):
    template_name = "mcwall/detail.html"

    def get(self, request, uid: uuid.UUID):
        return self.render(image=ImageModel.objects.get(pk=uid))
