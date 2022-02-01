from django.utils.translation import gettext_lazy as _
from frontend.models import Feedback
from django.forms import ModelForm, Textarea, TextInput, EmailInput


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_message', 'email', 'given_by', 'about']
        labels = {
            'feedback_message': _('आभिप्राय'),
            'given_by': _('आपले नाव'),
            'email': _('आपला ईमेल'),
        }
        widgets = {
            'given_by': TextInput({'class': 'form-control'}),
            'email': EmailInput({'class': 'form-control'}),
            'feedback_message': Textarea({'cols': 30, 'rows': 10, 'class': 'form-control'}),
            'about': TextInput({'type': 'hidden'})
        }
