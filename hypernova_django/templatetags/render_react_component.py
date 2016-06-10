from django import template
from django.utils.safestring import mark_safe

from ..models import (
    Renderer,
)

register = template.Library()

renderer = Renderer({
    'url': 'http://localhost:3553/batch',
})


@register.simple_tag
def render_react_component(component, props={}):
    html = renderer.render({component: props})

    return mark_safe(html)
