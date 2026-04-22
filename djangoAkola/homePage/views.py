# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "homePage/index.html", context)
    #return HttpResponse("Hello, world. You're at the HomePage index.")
