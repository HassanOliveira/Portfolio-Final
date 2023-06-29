from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def about_me(request):
    return render(request, 'base/about_me.html')

def projects(request):
    return render(request, 'base/projects.html')

def photos(request):
    return render(request, 'base/photos.html')

def blog(request):
    return render(request, 'base/blog.html')

def contact(request):
    return render(request, 'base/contact.html')

def construction(request):
    return render(request, 'base/construction.html')


def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER, 
            ['hassan_bittencourt@hotmail.com']
        )

        email.fail_silently = False
        email.send()

    return render(request, 'base/email_sent.html')