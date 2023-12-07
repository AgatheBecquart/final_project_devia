from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def hello(request):
    return render(request, 'hello.html')