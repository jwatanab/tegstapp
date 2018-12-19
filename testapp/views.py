from django_user_agents.utils import get_user_agent
from django.template.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import CreateView, TemplateView 
from .models import Account
from .forms import AccountForm

class LoginCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_user_agent(self.request).is_pc:
            context['is_pc'] = True 

        return context

def operation_check(request):
    if not request.method == 'POST':
        return redirect('/login', pk=1) # error Render

    request.session = request.POST

    context = {}
    context['is_pc'] = isPc(request)

    return render(request, 'main.html', context)

def isPc(request):
    return get_user_agent(request).is_pc
