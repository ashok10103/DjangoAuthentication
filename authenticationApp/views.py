from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

@login_required
def home(request):
    return (request,'index.html')