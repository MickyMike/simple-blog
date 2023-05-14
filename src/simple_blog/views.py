from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Hello World</h1>")
