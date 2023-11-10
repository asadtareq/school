from django.contrib import admin
from student.models import student
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=('name','class_name','roll','mobile','gender')
admin.site.register(student,studentAdmin)