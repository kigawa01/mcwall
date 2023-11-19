import django.forms

from mcwall import models


class ImageForm(django.forms.ModelForm):
    class Meta:
        model = models.ImageModel
        fields = (
            "name",
            "description",
            "file",
        )
