from django.urls import path
from frontend import views
from django.conf import settings
from django.conf.urls.static import static

app_name="frontend"
urlpatterns = [
    path('notices', views.notices, name="notices"),
    path('feedback', views.feedback, name="feedback"),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)