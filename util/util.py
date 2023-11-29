import abc
import hashlib

from django.shortcuts import render
from django.views import View


class BaseView(View):
    @property
    @abc.abstractmethod
    def template_name(self):
        pass

    def render(self, **context):
        return render(self.request, self.template_name, context)


class Hash:
    """hashを扱うクラス
    """

    @staticmethod
    def hash(value: any) -> str:
        """hashを行う
        """
        return hashlib.sha512(str(value).encode("utf-8")).hexdigest()
