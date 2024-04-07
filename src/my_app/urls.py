from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFDocumentViewSet

router = DefaultRouter()
router.register(r'pdf-cv', PDFDocumentViewSet)
    path('api/', include(router.urls)),
"""





urlpatterns = [
    path('api/projects', views.ProjectsView.as_view()),
    path('api/cv', views.Cv.as_view()),
    path('api/language-icons', views.LanguageIconView.as_view()),
    path("api/code-snippets", views.CodeSnippetsView.as_view()),
    path("api/skills", views.SkillsView.as_view()),
    path("api/my-languages", views.MyLanguageView.as_view()),
    path("api/frameworks", views.FrameworksView.as_view()),
    path("api/communication-icons", views.CommunicationIconsView.as_view()),
    path("api/job-tasks", views.JobTaskView.as_view()),
    path("api/work-historys", views.WorkHistoryView.as_view()),
    path("api/trainings", views.TrainingsView.as_view()),
    path("api/accomplishments", views.AccomplishmentsView.as_view()),
    path('api-token-auth', obtain_auth_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api/language-icons", views.LanguageIconViewSet, basename="language-icons")
router.register("api/projects", views.ProjectsViewSet, basename="projects")
router.register("api/code-snippets", views.CodeSnippetsView, basename="code-snippets")
router.register("api/skills", views.SkillsView, basename="skills")
router.register("api/my-languages", views.MyLanguageView, basename="my-languages")
router.register("api/frameworks", views.FrameworksView, basename="frameworks")
router.register("api/communication-icons", views.CommunicationIconsView, basename="communication-icons")
router.register("api/job-tasks", views.JobTaskView, basename="job-tasks")
router.register("api/work-historys", views.WorkHistoryView, basename="work-historys")
router.register("api/trainings", views.TrainingsView, basename="trainings")
router.register("api/accomplishments", views.AccomplishmentsView, basename="accomplishments")
"""