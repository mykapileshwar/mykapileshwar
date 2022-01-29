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
    path('notices', views.notices, name="notice"),
    path('feedback', views.feedback, name="feedback"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)