from django.contrib import admin
from membership.models import Course, CourseModule, Membership



@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = "course_name","is_premium","slug"

@admin.register(CourseModule)
class AdminC(admin.ModelAdmin):
    list_display = "course","course_module_name"

@admin.register(Membership)
class AdminProfile(admin.ModelAdmin):
    list_display = "user","pro_expire_date","subscription_type"