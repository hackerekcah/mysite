from django.shortcuts import render
from application.models import Test
# Create your views here.
from django.http import HttpResponse

from django.template import RequestContext, loader
from django.http import Http404

def index1(request):
    return render(request, 'application/application1.html', {})

def index2(request):
    return render(request, 'application/application2.html', {})

def submit(request):

    postList = request.POST.items()
    return render(request, 'application/submit_result.html', {"postList": postList})

def to_db(request):

    postList = request.POST
    newApt = Test(surname=postList["applicant.lastName"],given_name=postList["applicant.lastName"])
    newApt.save()
    return render(request, 'application/submit_result.html', {"postList": postList.items()})
