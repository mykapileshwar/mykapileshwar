from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "frontend/index.html")

def grampanchayat(request):
    return render(request, "frontend/Grampanchayat.html")

def geographical(request):
    return render(request, "frontend/Bhaugolic.html")

def educational(request):
    return render(request, "frontend/Shikshanvyavsay.html")

def religious(request):
    return render(request, "frontend/dharmik.html")

def tourism(request):
    return render(request, "frontend/Paryatan.html")

def cultural(request):
    return render(request, "frontend/Saunsrutik.html")