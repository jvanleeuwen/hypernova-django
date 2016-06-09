# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Renderer,
)


class RendererCreateView(CreateView):

    model = Renderer


class RendererDeleteView(DeleteView):

    model = Renderer


class RendererDetailView(DetailView):

    model = Renderer


class RendererUpdateView(UpdateView):

    model = Renderer


class RendererListView(ListView):

    model = Renderer

