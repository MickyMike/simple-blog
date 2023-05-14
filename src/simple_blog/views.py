from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello World</h1>")


def contact_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Our contact</h1>")


def about_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>About the page</h1>")