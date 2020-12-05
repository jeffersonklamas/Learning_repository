from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, Django! é o Jefferson Klamas</h1>")
