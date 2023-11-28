import hashlib

from django.views.generic import TemplateView


class BaseView(TemplateView):
    def render(self, kwargs: dict, **context):
        return self.render_to_response({
            **super().get_context_data(**kwargs),
            **context
        })
class Hash:
    """hashを扱うクラス
    """

    @staticmethod
    def hash(value: any) -> str:
        """hashを行う
        """
        return hashlib.sha512(str(value).encode("utf-8")).hexdigest()
