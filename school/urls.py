from django.contrib import admin
#from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notice import views as nv
from teacher import views as tv
from student import views as sv
admin.site.site_header="Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', nv.index, name="index"),
    path("notice/", nv.notice_view, name="notice"),
    path("notice/<int:id>", nv.notice_details, name="notice_details"),
    path("teacher/", tv.teacher_view, name="teacher"),
    path("student/", sv.student_view, name="student"),
    path("gallery/", nv.gallery_view, name="gallery"),
    path("smc/", nv.smc_view, name="smc"),
    path("club/", nv.club_view, name="club"),
    path("school-result/", nv.result_view, name="school-result"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
