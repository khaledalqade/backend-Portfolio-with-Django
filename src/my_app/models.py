from django.db import models
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User




class LanguageIcon(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='language_icon/', null=True, blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    Type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    theDescription = models.TextField()
    Image = models.ImageField(upload_to='projects/')
    crs = models.CharField(max_length=100)
    language_icons = models.ManyToManyField(LanguageIcon)

    def __str__(self):
        return self.name



class CodeSnippet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    crs = models.CharField(max_length=100)
    language_icons = models.ManyToManyField(LanguageIcon)


    def __str__(self):
        return self.name
    




class CommunicationIcon(models.Model):
    image = models.ImageField(upload_to='communication_icon/')
    crs = models.CharField(max_length=50)

    def __str__(self):
        return self.crs
    



class Skill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill





class MyLanguage(models.Model):
    image = models.ImageField(upload_to='my_language_icon/')
    percentage = models.IntegerField()
    color = models.CharField(max_length=7)

    def __str__(self):
        return str(self.percentage) + "% - " + self.color
    



class Framework(models.Model):
    image = models.ImageField(upload_to='my_framework_icon/')
    percentage = models.IntegerField()
    color = models.CharField(max_length=7)

    def __str__(self):
        return str(self.percentage) + "% - " + self.color
    



class JobTask(models.Model):
    job_tasks = models.TextField()


class WorkHistory(models.Model):
    date = models.CharField(max_length=100)
    company = models.TextField()
    job_tasks = models.ManyToManyField(JobTask)

    def __str__(self):
        return self.date
    





class Training(models.Model):
    training = models.CharField(max_length=100)

    def __str__(self):
        return self.training
    



class Accomplishment(models.Model):
    completion = models.CharField(max_length=100)

    def __str__(self):
        return self.completion
    



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)





class PDFDocument(models.Model):
    pdf_file = models.FileField(upload_to='cv_pdfs/')