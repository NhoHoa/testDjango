from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Cac ban. Cac ban cos khoe khong")