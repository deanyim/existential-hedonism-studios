from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Will. You're at the police station.")
