from django.contrib import admin
from .models import Accomplishment, Training, JobTask, WorkHistory, Framework, MyLanguage, Skill, CommunicationIcon, CodeSnippet, Project, LanguageIcon, PDFDocument


# Register your models here.

admin.site.register(Accomplishment)
admin.site.register(Training)
admin.site.register(JobTask)
admin.site.register(Framework)
admin.site.register(MyLanguage)
admin.site.register(Skill)
admin.site.register(CommunicationIcon)
admin.site.register(CodeSnippet)
admin.site.register(LanguageIcon)
admin.site.register(Project)
admin.site.register(WorkHistory)
admin.site.register(PDFDocument)
