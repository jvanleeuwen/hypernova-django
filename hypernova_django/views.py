# -*- coding: utf-8 -*-
# from django.http import (
#     HttpResponse
# )
#
# from django.views.generic import (
#     TemplateView
# )
#
# from .models import (
#     Renderer,
# )
#
#
# renderer = Renderer({
#     'url': 'http://localhost:3553/batch',
# })
#
#
# class RendererListView(TemplateView):
#     template_name = 'hypernova_django/base.html'
#
#     def render_to_response(self, context, **response_kwargs):
#         jobs = {
#             'Component': {'prop': 'value'},
#         }
#         return HttpResponse(renderer.render(jobs))
#
