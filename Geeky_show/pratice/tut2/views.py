from django.shortcuts import render,HttpResponse
def second(request):
    a="<h1>This is the second page</h1>"
    return HttpResponse(a)
