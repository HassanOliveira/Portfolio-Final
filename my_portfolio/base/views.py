from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from base.models import Projects, Category, TimelineItem, CV


def home(request):
    projects = Projects.objects.order_by("date_project").filter(published=True)
    timeline_items = TimelineItem.objects.all()
    categories = Category.objects.all()
    cv = CV.objects.first()
    return render(request, 'base/home.html', {"cards": projects, 'timeline_items': timeline_items, 'cv': cv, 'categories': categories})

def project_info(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, 'base/project_info.html', {"project": project})

def construction(request):
    return render(request, 'base/construction.html')