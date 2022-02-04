import json
from frontend.models import Feedback, Notice
from frontend.forms import FeedbackForm
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from kapileshwar.settings import DEFAULT_FROM_EMAIL


@require_http_methods(["GET"])
def notices(request):
    notices = Notice.objects.all()
    serialized_notices = []
    for notice in  notices:
        serialized_notices.append(notice.serialized_notice())
    return JsonResponse({"notices":serialized_notices})

@csrf_exempt
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
        return HttpResponseNotAllowed(["POST"])
