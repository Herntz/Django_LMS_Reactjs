from django.contrib import admin
from .models import *

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone','qualification','adress') 
    list_filter = ('full_name', 'qualification')
    search_fields = ('full_name', 'phone','qualification')
    
admin.site.register(Course)
admin.site.register(CourseCategory)
admin.site.register(Student)