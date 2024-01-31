from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['teacher_name','student_name','schedule_types','schedule_status','description','time','cancel']

    def teacher_name (self,obj):
        return f"{obj.teacher.user.first_name} {obj.teacher.user.last_name}"

    def student_name (self,obj):
        return f"{obj.student.user.first_name} {obj.student.user.last_name}"

admin.site.register(Schedule,ScheduleAdmin)