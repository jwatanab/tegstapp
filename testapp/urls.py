# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import LoginCreateView

urlpatterns = [
    url(r'^create$', LoginCreateView.as_view()), 
]
