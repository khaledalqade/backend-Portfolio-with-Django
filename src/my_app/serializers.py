from rest_framework import serializers
from .models import Project, CommunicationIcon, Skill, MyLanguage, CodeSnippet, Framework, WorkHistory, Training, Accomplishment, LanguageIcon, JobTask, PDFDocument


class CommunicationIconsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationIcon
        fields = '__all__'

    
class SkillsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Skill
        fields = '__all__'





class LanguagesSerializer(serializers.ModelSerializer):
     class Meta:
        model = MyLanguage
        fields = '__all__'


from rest_framework import serializers
from .models import CodeSnippet

class LanguageIconSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageIcon
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    language_icons = serializers.SerializerMethodField()

    def get_language_icons(self, obj):
        request = self.context.get('request')
        language_icons = obj.language_icons.all()
        return [
            {
                'id': language_icon.id,
                'name': language_icon.name,
                'image_url': request.build_absolute_uri(language_icon.icon.url)
            }
            for language_icon in language_icons
        ]

    class Meta:
        model = Project
        fields = '__all__'



class CodeSnippetsSerializer(serializers.ModelSerializer):
    language_icons = serializers.SerializerMethodField()
     
    def get_language_icons(self, obj):
        request = self.context.get('request')
        language_icons = obj.language_icons.all()
        return [
            {
                'id': language_icon.id,
                'name': language_icon.name,
                'image_url': request.build_absolute_uri(language_icon.icon.url)
            }
            for language_icon in language_icons
        ]
     

    class Meta:
        model = CodeSnippet
        fields = '__all__'





class FrameworksSerializer(serializers.ModelSerializer):
     class Meta:
        model = Framework
        fields = '__all__'




class WorkHistorySerializer(serializers.ModelSerializer): 
    job_tasks = serializers.SerializerMethodField()

    def get_job_tasks(self, obj):
        request = self.context.get('request')
        job_tasks = obj.job_tasks.all()
        return [
            {
                'id': job_task.id,
                'job_tasks': job_task.job_tasks,
            }
            for job_task in job_tasks
        ]
    class Meta:
        model = WorkHistory
        fields = '__all__'


class TrainingsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Training
        fields = '__all__'



class AccomplishmentsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Accomplishment
        fields = '__all__'



class JobTaskSerializer(serializers.ModelSerializer):
     class Meta:
        model = JobTask
        fields = '__all__'




class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = '__all__'