# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^$",
        view=views.RendererListView.as_view(),
        name='Renderer_list',
    ),
]
