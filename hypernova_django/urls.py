# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Renderer/~create/$",
        view=views.RendererCreateView.as_view(),
        name='Renderer_create',
    ),
    url(
        regex="^Renderer/(?P<pk>\d+)/~delete/$",
        view=views.RendererDeleteView.as_view(),
        name='Renderer_delete',
    ),
    url(
        regex="^Renderer/(?P<pk>\d+)/$",
        view=views.RendererDetailView.as_view(),
        name='Renderer_detail',
    ),
    url(
        regex="^Renderer/(?P<pk>\d+)/~update/$",
        view=views.RendererUpdateView.as_view(),
        name='Renderer_update',
    ),
    url(
        regex="^Renderer/$",
        view=views.RendererListView.as_view(),
        name='Renderer_list',
    ),
	]
