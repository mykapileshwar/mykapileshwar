from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary.api import delete_resources

# Create your models here.
class Notice(models.Model):
    notice_message = models.CharField(max_length=200)
    issued_on = models.DateTimeField(auto_created=True, auto_now=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = CloudinaryField(blank=True)

    def has_attatchment(self) -> bool:
        """Returns True if notice has an attachment otherwise returns False."""
        return (False, True)[self.attachment.url is not None]

    def serialized_notice(self):
        return {
            "notice_message":self.notice_message,
            "attachment":self.attachment.url
        }

    def delete(self, *args, **kwargs):
        print("deleting from cloudinary...")
        response = delete_resources(public_ids=self.attachment)
        print(response)
        return super().delete(*args, **kwargs)

    def __str__(self) -> str:
        super().__str__()
        return self.notice_message[:20] + " issued by " + self.issued_by.username

class Feedback(models.Model):

    FEEDBACK_SECTIONS = [
        ("Grampanchayat", "Grampanchayat"),
        ("Education", "Education"),
        ("Tourism", "Tourism"),
    ]

    feedback_message = models.CharField(max_length=250)
    given_on = models.DateTimeField(auto_created=True, auto_now=True)
    given_by = models.CharField(max_length=40)
    email = models.EmailField()
    about = models.CharField(max_length=14, choices=FEEDBACK_SECTIONS, default="Grampanchayat")

    def __str__(self) -> str:
        super().__str__()
        return self.feedback_message[:30] + " given by " + self.given_by