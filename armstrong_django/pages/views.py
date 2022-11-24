from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.views.generic import TemplateView


def homepage_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world!")


class HomepageView(TemplateView):
    template_name = "homepage.html"


class AboutView(TemplateView):
    template_name = "about.html"
