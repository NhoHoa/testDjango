from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, My wife is Do thi Lan Phuong")