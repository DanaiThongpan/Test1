from django.contrib import admin

# Register your models here.
from .models import  UserRecruitment_Announcer

# class UserFarmerAdmin(admin.ModelAdmin):
#     list_display = ['username', 'email', 'first_name', 'last_name', 'is_student', 'is_recruitment_announcer']  # สังเกตุได้ที่ 'is_farmer', 'is_driver'

# admin.site.register(UserStudent, UserFarmerAdmin)

class UserDriverAdmin(admin.ModelAdmin):
    list_display = ['username', 'email',  'first_name', 'last_name','is_student', 'is_recruitment_announcer']  # สังเกตุได้ที่ 'is_farmer', 'is_driver'

admin.site.register(UserRecruitment_Announcer, UserDriverAdmin)