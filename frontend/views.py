import json
from django.shortcuts import render
from frontend.models import Feedback, Notice
from frontend.forms import FeedbackForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import send_mail, BadHeaderError

from kapileshwar.settings import DEFAULT_FROM_EMAIL

def homepage(request):
    return render(request, "frontend/index.html")


def grampanchayat(request):
    notices = Notice.objects.all()
    context = {
        "notices": notices,
        "feedback_form": FeedbackForm(initial={"about": "Grampanchayat"})
    }
    return render(request, "frontend/Grampanchayat.html", context)


def geographical(request):
    return render(request, "frontend/Bhaugolic.html")


def educational(request):
    return render(request, "frontend/Shikshanvyavsay.html", {"feedback_form": FeedbackForm(initial={"about": "Education"})})


def religious(request):
    return render(request, "frontend/dharmik.html")


def tourism(request):
    return render(request, "frontend/Paryatan.html", {"feedback_form": FeedbackForm(initial={"about": "Educational"})})


def cultural(request):
    return render(request, "frontend/Saunsrutik.html")


def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(json.loads(request.body))

        # Validate and save feedback
        if form.is_valid():
            print("valid feedback")
            message = form.cleaned_data['feedback_message']
            about = form.cleaned_data['about']
            given_by = form.cleaned_data['given_by']
            new_feedback = Feedback(feedback_message=message, given_by=given_by, about=about)
            new_feedback.save()

            # Create email
            subject = f"Feedback from {new_feedback.given_by} about {new_feedback.about}"
            if new_feedback.about in ["Grampanchayat", "Tourism"]:
                recipient_list = ['akshaymusale5641@gmail.com']
            elif new_feedback.about == "Education":
                recipient_list = ['osgsmail19@gmail.com']
            else:
                return HttpResponseBadRequest()

            # Send feedback through email
            try:
                print("sending email....")
                send_mail(subject, message, from_email=DEFAULT_FROM_EMAIL, recipient_list=recipient_list)
            except BadHeaderError:
                return JsonResponse({"error": "Invalid header found."})
        else:
            return HttpResponseBadRequest()
        return JsonResponse({"success": "Email sent successfully"})
