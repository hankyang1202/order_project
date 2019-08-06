import re
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic.base import View, TemplateResponseMixin

LOGIN_URL = '/member/login/'
REDIRECT_PAGE = '/member/(login/|logout/|register/|password/reset/\w+/)'


def get_path(url):
    temp = url.split('/')
    return '/'+'/'.join(temp[3:])


class BaseView(View):
    HOME_PAGE = '/'

    def get_previouse_page(self, request):
        url = request.session.get('referer', '/')
        return url


class BaseTemplateView(BaseView, TemplateResponseMixin):
    login_required = login_required()

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            referer = request.session.get('referer', '')
            prog = re.compile(REDIRECT_PAGE)
            if not bool(prog.match(request.get_full_path())):
                referer = request.get_full_path()
            request.session['referer'] = referer
        return super(BaseTemplateView, self).dispatch(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return super(BaseTemplateView, self).render_to_response(
            context, **response_kwargs
        )
