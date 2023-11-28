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


class A(django.forms.Form):
    text = django.forms.CharField()
    replace_before = django.forms.CharField()
    replace_after = django.forms.CharField()
