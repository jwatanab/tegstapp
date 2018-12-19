from django_user_agents.utils import get_user_agent
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView 
from .models import Account
from .forms import AccountForm

class LoginCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "login.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_user_agent(self.request).is_pc:
            context['is_pc'] = True 

        return context
