from utils.base_view import BaseTemplateView


class IndexView(BaseTemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        try:
            context = {}
        except Exception as e:
            raise e
        else:
            return self.render_to_response(context=context)
