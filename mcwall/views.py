from django.views import generic

from mcwall import models


# Create your views here.

class Index(generic.ListView):
    template_name = "index.html"
    model = models.ImageModel
