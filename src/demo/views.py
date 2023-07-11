from django.shortcuts import render
from .google_bard import chat, get_response
from django.http import HttpResponse
import json


def index(request):
    return render(request, "index.html")


def google_bard_response(request):
    
    response = get_response(request.GET.get('prompt'))
    # print(response)

    return HttpResponse(json.dumps(response), content_type='application/json')
