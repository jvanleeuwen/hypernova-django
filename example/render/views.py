from django.views.generic import (
    TemplateView
)


class TestView(TemplateView):
    template_name = 'render/base.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)

        context.update({
            'component': 'Component',
            'props': {'prop': 'value'},
        })

        return context
