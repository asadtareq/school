from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
# Create your views here.

#from django.views.generic import ListView, DetailView

# Create your views here.
def student_view(request):
    show_student=student.objects.all().order_by('class_name','roll')
    return render(request, "students/student.html",{'sv': show_student})