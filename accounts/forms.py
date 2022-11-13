import posixpath

from django import forms
from django.forms import ModelForm
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from accounts.models import User
from eshop_project import settings


def thumbnail(image_path, width, height):
    absolute_url = posixpath.join(settings.MEDIA_URL, image_path)
    return f'<img src="{absolute_url}" alt="{image_path}", width={width}, height={height}>'


class ImageWidget(forms.ClearableFileInput):
    template = '<div>%(image)s</div>' \
               '<div>%(clear_template)s</div>' \
               '<div>%(input)s</div>'
    initial_text = ''
    template_name = 'widgets/file_image_input.html'

    def __init__(self, attrs=None, template=None, width=150, height=150):
        if template is not None:
            self.template = template
        self.width = width
        self.height = height
        super(ImageWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        input_html = super(forms.FileInput, self).render(name, value, attrs)
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }

        if not self.is_required:
            checkbox_name = self.clear_checkbox_name(name)
            checkbox_id = self.clear_checkbox_id(checkbox_name)
            substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
            substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
            substitutions['clear'] = forms.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})

        # input_html = super(forms.ClearableFileInput, self).render(name, value, attrs)
        if value and hasattr(value, 'width') and hasattr(value, 'height'):
            image_html = thumbnail(value.name, self.width, self.height)
            output = self.template % {
                'input': input_html,
                'image': image_html,
                'clear_template': '',
            }
        else:
            output = input_html
        return mark_safe(output)


class ProfileForm(ModelForm):
    email = forms.EmailField(disabled=True)
    last_login = forms.DateTimeField(disabled=True)

    class Meta:
        model = User
        fields = [
            "avatar",
            "email",
            "last_login",
            "first_name",
            "last_name",
            "street",
            "city",
            "zip_code",
            "country",
            "phone",
            "communication_channel",
        ]
        widgets = {
            'avatar': ImageWidget
        }


class MyLoginForm(forms.Form):
    pass