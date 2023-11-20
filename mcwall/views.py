from django.urls import reverse_lazy
from django.views import generic

from mcwall import models, forms


# Create your views here.

class Index(generic.ListView):
    template_name = "index.html"
    model = models.ImageModel
    ordering = "-created_at"
    paginate_by = 12


class Create(generic.CreateView):
    template_name = "create.html"
    form_class = forms.ImageForm
    model = models.ImageModel
    success_url = reverse_lazy("mcwall:index")
