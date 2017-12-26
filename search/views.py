from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.i

def index(request):
    return HttpResponse("Hii, you are owl's homepage")
