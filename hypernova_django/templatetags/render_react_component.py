from django import template
from django.utils.safestring import mark_safe

from hypernova_django.plugins.dev_mode_plugin import (
    dev_mode_plugin
)

from ..models import (
    Renderer,
)

register = template.Library()

renderer = Renderer({
    'url': 'http://localhost:3553/batch',
    'plugins': dev_mode_plugin,
})


@register.simple_tag
def render_react_component(component, props={}):
    html = renderer.render({component: props})

    return mark_safe(html)
