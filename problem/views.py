from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, My Name is Le Nho Hoa")