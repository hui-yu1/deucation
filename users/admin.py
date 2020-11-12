from django.contrib import admin
from .models import UserProfile, StudentClass, Student, Teacher, Course

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", "email")
    search_fields = list_display

class StudentClassAdmin(admin.ModelAdmin):
    list_display = ("cla_major", "cla_name", "cla_number")
    search_fields = list_display

class StudentAdmin(admin.ModelAdmin):
    list_display = ("stu_name", "stu_age", "stu_gender", "stu_address", "stu_time", "stu_major", "stu_class")
    search_fields = list_display

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("tea_name", "tea_phone", "tea_email")
    search_fields = list_display

class CourseAdmin(admin.ModelAdmin):
    list_display = ("cou_name", "cou_times", "cou_duration", "cou_teacher", "cou_class")
    search_fields = list_display

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(StudentClass, StudentClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
