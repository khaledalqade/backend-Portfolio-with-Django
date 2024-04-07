from .serializers import SkillsSerializer, LanguageIconSerializer, LanguagesSerializer, CodeSnippetsSerializer, ProjectsSerializer, FrameworksSerializer, AccomplishmentsSerializer, TrainingsSerializer, WorkHistorySerializer, JobTaskSerializer
from .models import Project, CommunicationIcon, Skill, MyLanguage, CodeSnippet, Framework, WorkHistory, Training, Accomplishment, LanguageIcon, JobTask
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .serializers import CommunicationIconsSerializer

class CommunicationIconsView(generics.ListAPIView): 
    queryset = CommunicationIcon.objects.all()
    serializer_class = CommunicationIconsSerializer


class SkillsView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer



class LanguageIconView(generics.ListAPIView):
    queryset = LanguageIcon.objects.all()
    serializer_class = LanguageIconSerializer
    authentication_classes = [TokenAuthentication]



class MyLanguageView(generics.ListAPIView):
    queryset = MyLanguage.objects.all()
    serializer_class = LanguagesSerializer



class CodeSnippetsView(generics.ListAPIView):
    queryset = CodeSnippet.objects.all()
    serializer_class = CodeSnippetsSerializer



class ProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
    authentication_classes = [TokenAuthentication]






class FrameworksView(generics.ListAPIView):
    queryset = Framework.objects.all()
    serializer_class = FrameworksSerializer




class AccomplishmentsView(generics.ListAPIView):
    queryset = Accomplishment.objects.all()
    serializer_class = AccomplishmentsSerializer




class TrainingsView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingsSerializer




class WorkHistoryView(generics.ListAPIView):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer




class JobTaskView(generics.ListAPIView):
    queryset = JobTask.objects.all()
    serializer_class = JobTaskSerializer

from .serializers import PDFDocumentSerializer
from .models import PDFDocument


class Cv(generics.ListAPIView):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

"""
from rest_framework.viewsets import ModelViewSet

class PDFDocumentViewSet(ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer
"""