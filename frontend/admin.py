from django.contrib import admin
from frontend.models import *

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_message', 'issued_on', 'issued_by')


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Feedback)