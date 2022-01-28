from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

def user_directory_path(instance, filename):
    # file will be uploaded to uploads/user_<id>/<filename>
    return 'uploads/user_{0}/{1}'.format(instance.issued_by.id, filename)

# Create your models here.
class Notice(models.Model):
    notice_message = models.CharField(max_length=200)
    issued_on = models.DateTimeField(auto_created=True, auto_now=True)
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = CloudinaryField()

    def has_attatchment(self) -> bool:
        """Returns True if notice has an attachment otherwise returns False."""
        return (False, True)[self.attachment.url is not None]

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