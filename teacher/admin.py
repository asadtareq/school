from django.contrib import admin
from teacher.models import teacher
# Register your models here.

# Register your models here.
class teacherAdmin(admin.ModelAdmin):
    list_display=('name','image','designation','subject','mobile')
admin.site.register(teacher,teacherAdmin)