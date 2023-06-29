from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about_me/', views.about_me, name="about me"),
    path('projects/', views.construction, name="projects"),
    path('photos/', views.construction, name="photos"),
    path('blog/', views.construction, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('send_email/', views.sendEmail, name="send_email"),
]