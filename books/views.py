from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def search_form(request):
    return render(request,'books/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request,'books/search_results.html',
            {'books': books, 'query': q})
    else:
        return render(request,'books/search_form.html',{'error':True}) 
'''
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''
