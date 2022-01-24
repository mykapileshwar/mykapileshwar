from django.utils.translation import gettext_lazy as _
from frontend.models import Notice, Feedback
from django.forms import ModelForm, Textarea, TextInput


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_message', 'given_by', 'about']
        labels = {
            'feedback_message': _('आभिप्राय'),
            'given_by': _('आपले नाव'),
        }
        widgets = {
            'given_by': TextInput({'class': 'form-control'}),
            'feedback_message': Textarea({'cols': 30, 'rows': 10, 'class': 'form-control'}),
            'about': TextInput({'type': 'hidden'})
        }
