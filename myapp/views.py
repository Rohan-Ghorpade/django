from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    return HttpResponse("<h1>welcome to django session 1</h1>")

def view2(request):
    return HttpResponse("<h1>welcome to django session 2</h1>")

def view3(request):
    return HttpResponse("<h1>welcome to django session 3</h1>")

def view4(request):
    return HttpResponse("<h1>welcome to django session 4</h1>")

def view5(request):
    return HttpResponse("<h1>welcome to django session 5</h1>")

def view6(request):
    return HttpResponse("<h1>welcome to django session 6</h1>")

def view7(request):
    return HttpResponse("<h1>welcome to django session 7</h1>")