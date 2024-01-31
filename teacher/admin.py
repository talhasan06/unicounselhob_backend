from django.contrib import admin
from .models import Teacher,AvailableTime
# Register your models here.

class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name']

    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(AvailableTime)
