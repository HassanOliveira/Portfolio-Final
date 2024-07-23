from django.db import models

from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Projecty(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    category = models.ManyToManyField(Category)
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=False)
    date_project = models.DateTimeField(default=datetime.now, blank=False)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    image = models.ImageField(upload_to='timeline/', default='timeline/construction.jpg')
    company = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title
    

class CV(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='cv_files/')

    def __str__(self):
        return self.title
