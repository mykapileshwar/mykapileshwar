from django.urls import path
from frontend import views

app_name="frontend"
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('grampanchayat', views.grampanchayat, name="grampanchayat"),
    path('geographical-information', views.geographical, name="geographical"),
    path('education-and-business', views.educational, name="educational"),
    path('religious-information', views.religious, name="religious"),
    path('tourism-information', views.tourism, name="tourism"),
    path('cultural-information', views.cultural, name="cultural"),
]