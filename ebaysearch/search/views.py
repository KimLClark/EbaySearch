from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    n = 'Bob'
    animals = ['Zebra', 'Cat', 'Dog']
    return render(request, 'search/index.html', context={'name':n, 'animals':animals})