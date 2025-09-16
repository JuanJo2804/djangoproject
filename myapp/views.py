from django.http import HttpResponse


# Create your views here.
def hello(request, username):
    print(username)
    return HttpResponse("Hello, world!")


def about(request):
    return HttpResponse("About")
