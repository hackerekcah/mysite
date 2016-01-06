from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.template import RequestContext, loader
from django.http import Http404

def index(request):
    return render(request, 'application/application.html', {})


