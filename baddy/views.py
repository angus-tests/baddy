from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


def index(request: HttpRequest) -> HttpResponse:
    """
    Render the index page.
    :param request:
    :return:
    """
    return render(request, "baddy/index.html")
