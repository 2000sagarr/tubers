from django.urls import path
from . import views

urlpatterns=[
    #method are defined in veiws.py file
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
]