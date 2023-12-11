from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project_info/<int:project_id>/', views.project_info, name='project_info'),
]