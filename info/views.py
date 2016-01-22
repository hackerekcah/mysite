from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext, loader
from django.http import Http404

from info.models import Applicant


def index(request):
    return render(request, 'info/info_index.html', {})


def to_db(request):
    postList = request.POST
    # newApt = Applicant(surname=postList["applicant.surname"],given_name=postList["applicant.given_name"])
    # newApt.save()
    return render(request, 'info/submit_result.html', {"postList": postList.items()})

def test(request):
    return render(request, 'info/test.html',{})
def validate(request):
    return render(request, 'info/validate.html',{})

