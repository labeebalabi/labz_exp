from django.shortcuts import render
from django.http.response import HttpResponse

def test(request):
    return HttpResponse(" Hello world..........@")
# Create your views here.
