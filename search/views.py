from django.shortcuts import render
from django.http import HttpResponse
import search.EYE.facade as eye 


def index(request):
    query = request.GET.get('query','')
    query=query.replace("'","")
    query=query.replace('"','')

    if query=='':
        return HttpResponse("Blank query recieved")
    else:
        return HttpResponse(eye.find(query))

    return HttpResponse("Hii, you are owl's homepage")
