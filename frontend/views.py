from django.shortcuts import render
from frontend.models import Notice

# Create your views here.
def homepage(request):
    return render(request, "frontend/index.html")


def grampanchayat(request):
    notices = Notice.objects.all()
    return render(request, "frontend/Grampanchayat.html", {"notices": notices})


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
