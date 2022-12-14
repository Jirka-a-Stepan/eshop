from django import template
from django.contrib.auth.forms import AuthenticationForm


register = template.Library()


@register.inclusion_tag('login.html')
def render_login():
    form = AuthenticationForm()
    return {'form': form}
