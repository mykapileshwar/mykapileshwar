from django.contrib import admin
from frontend.models import *

admin.site.site_header = "Kapileshwar Website Administration"
admin.site.site_url = "https://mykapileshwar.github.io"

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_message', 'issued_on', 'issued_by')
    fields = ['notice_message', 'attachment']
    
    # Set notice issuer's name as name of logged in user
    def save_model(self, request, obj, form, change) -> None:
        obj.issued_by = request.user
        return super().save_model(request, obj, form, change)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_message', 'given_by', 'given_on')


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Feedback, FeedbackAdmin)