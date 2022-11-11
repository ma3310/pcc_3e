from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def homepage_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")
