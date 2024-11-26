from django.http import HttpResponse

# Create your views here.

def my_blog(request):
    return HttpResponse("<h1>This is my blog!<h1>")
