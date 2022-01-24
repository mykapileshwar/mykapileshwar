from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

app_name="frontend"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('grampanchayat', views.grampanchayat, name="grampanchayat"),
    path('geographical-information', views.geographical, name="geographical"),
    path('education-and-business', views.educational, name="educational"),
    path('religious-information', views.religious, name="religious"),
    path('tourism-information', views.tourism, name="tourism"),
    path('cultural-information', views.cultural, name="cultural"),
    path('feedback', views.feedback, name="feedback"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)