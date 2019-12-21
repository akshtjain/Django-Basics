from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    response = HttpResponse("Hello World!")
    return response