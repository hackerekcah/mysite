from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'application/index.html', {"user":request.user})


def procedure(request):
    return render(request, 'application/application_procedure.html', {"user":request.user})


def contact_us(request):
    return render(request, 'application/contact_us.html', {"user":request.user})


def blank(request):
    if request.user.is_authenticated():

        return render(request, 'application/blank.html', {})
    else:
        return HttpResponseRedirect('/accounts/login')


def user_profile(request):
    if request.user.is_authenticated():
        return render(request, 'application/user_profile.html', {"user": request.user})
    else:
        return HttpResponseRedirect('/accounts/login')

def profile_change(request):
    if request.user.is_authenticated():
        user = User.objects.get(email = request.user.email)
        user.first_name = request.POST.get("first_name",None)
        user.last_name = request.POST.get("last_name",None)
        user.phone = request.POST.get("phone",None)
        user.save()
        print user.phone
        return render(request, 'application/user_profile.html', {"user": user})
    else:
        return HttpResponseRedirect('/accounts/login')


def apply_for_visa(request):
    if request.user.is_authenticated():

        return render(request, 'application/apply_for_visa.html', {})
    else:
        return HttpResponseRedirect('/accounts/login')


def application_status(request):
    if request.user.is_authenticated():

        return render(request, 'application/application_status.html', {})
    else:
        return HttpResponseRedirect('/accounts/login')


def test(request):
    return render(request, 'application/test.html', {})