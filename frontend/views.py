import json
from django.shortcuts import render
from frontend.models import Feedback, Notice
from frontend.forms import FeedbackForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_http_methods

from kapileshwar.settings import DEFAULT_FROM_EMAIL

@require_http_methods(["GET"])
def homepage(request):
    return render(request, "frontend/index.html")

@require_http_methods(["GET"])
def grampanchayat(request):
    notices = Notice.objects.all()
    context = {
        "notices": notices,
        "feedback_form": FeedbackForm(initial={"about": "Grampanchayat"})
    }
    return render(request, "frontend/grampanchayat.html", context)

@require_http_methods(["GET"])
def geographical(request):
    return render(request, "frontend/bhaugolic.html")

@require_http_methods(["GET"])
def educational(request):
    return render(request, "frontend/shikshanvyavsay.html", {"feedback_form": FeedbackForm(initial={"about": "Education"})})

@require_http_methods(["GET"])
def religious(request):
    return render(request, "frontend/dharmik.html")

@require_http_methods(["GET"])
def tourism(request):
    return render(request, "frontend/paryatan.html", {"feedback_form": FeedbackForm(initial={"about": "Educational"})})

@require_http_methods(["GET"])
def cultural(request):
    return render(request, "frontend/saunsrutik.html")

@require_http_methods(["POST"])
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(json.loads(request.body))

        # Validate and save feedback
        if form.is_valid():
            print("valid feedback")
            message = form.cleaned_data['feedback_message']
            about = form.cleaned_data['about']
            given_by = form.cleaned_data['given_by']
            email = form.cleaned_data['email']
            new_feedback = Feedback(feedback_message=message, given_by=given_by, about=about, email=email)
            new_feedback.save()

            # Get emails of users of relevant group
            group = Group.objects.filter(name=new_feedback.about).first()
            users = User.objects.filter(groups=group.id)
            emails = []
            for user in users:
                emails.append(user.email)

            # Create email
            subject = f"Feedback from {new_feedback.given_by} about {new_feedback.about}"
            email_body = f"{new_feedback.feedback_message} \nProvided Contact Email: {new_feedback.email}"

            # Send feedback through email
            try:
                print("sending email....")
                send_mail(subject=subject, message=email_body, from_email=DEFAULT_FROM_EMAIL, recipient_list=emails)
            except BadHeaderError:
                return JsonResponse({"error": "Invalid header found."})
        else:
            return HttpResponseBadRequest()
        return JsonResponse({"success": "Email sent successfully"})
    
    else:
        return HttpResponseBadRequest()
