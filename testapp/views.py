from django.shortcuts import render, redirect
from django.views.generic import TemplateView 

class TestTemplateView(TemplateView):
    template_name = "index.html"
