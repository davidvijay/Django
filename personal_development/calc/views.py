from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'Vijay'})

def add(request):
    value1 = int(request.POST["num1"])
    value2 = int(request.POST["num2"])
    result = value1+value2
    return render(request, 'add_result.html', {'res':result})
    