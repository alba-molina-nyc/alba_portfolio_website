from django.db import models
from django.urls import reverse

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    tech = models.TextField()
    demo = models.URLField()
    deployed = models.URLField()
    code = models.URLField()
    img = models.URLField()
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.TextField()
    writing = models.TextField()
    img = models.URLField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

class Quote(models.Model):
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()
    project_start_date = models.DateField()
    project_end_date = models.DateField()
    phone = models.TextField()
    project_details = models.TextField()

    def __str__(self):
        return self.email
