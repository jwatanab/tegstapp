# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import TestTemplateView

urlpatterns = [
    url(r'^', TestTemplateView.as_view()),
]
