from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from base.models import Project, Category, Experience, CV


def home(request):
    projects = Project.objects.order_by("date_project").filter(published=True)
    experiences = Experience.objects.all()
    categories = Category.objects.all()
    cv = CV.objects.first()
    return render(request, 'base/home.html', {"cards": projects, 'experiences': experiences, 'cv': cv, 'categories': categories})

def project_info(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'base/project_info.html', {"project": project})

def construction(request):
    return render(request, 'base/construction.html')