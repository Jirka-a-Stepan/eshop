from django import template
from django.contrib.auth.forms import AuthenticationForm

from accounts.views import login_request

register = template.Library()

@register.inclusion_tag('registration/login.html')
def render_login():
    form = login_request()
    return {'form': form}
