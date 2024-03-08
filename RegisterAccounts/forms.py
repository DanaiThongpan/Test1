# Accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import  UserRecruitment_Announcer

# class UserStudentRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, required=True, label='ชื่อ')  # เพิ่มชื่อ-สกุล
#     last_name = forms.CharField(max_length=100, required=True, label='สกุล')  # สกุล
#     address = forms.CharField(max_length=255, required=True, label='ที่อยู่')  # เพิ่มที่อยู่
#     phone = forms.CharField(max_length=15, required=True, label='เบอร์โทรศัพท์')  # เพิ่มเบอร์โทรศัพท์
#     id_student = forms.IntegerField(primary_key=True)
#     username = forms.CharField(max_length=20)
#     title_choices = [
#         ('นาย', 'นาย'),
#         ('นาง', 'นาง'),
#         ('นางนสาว', 'นางสาว'),
#     ]
#     title = forms.CharField(max_length=10, choices=title_choices, default="วิทยาศาสตร์")
#     email = forms.CharField(unique=True, max_length=30)
#     faculty_choices = [
#         ('วิทยาศาสตร์', 'วิทยาศาสตร์'),
#         ('คณะเกษตรศาสตร์', 'คณะเกษตรศาสตร์'),
#         ('คณะวิศวกรรมศาสตร์', 'คณะวิศวกรรมศาสตร์'),
#         ('คณะศิลปศาสตร์', 'คณะศิลปศาสตร์'),
#         ('คณะเภสัชศาสตร์', 'คณะเภสัชศาสตร์'),
#         ('คณะบริหารศาสตร์', 'คณะบริหารศาสตร์'),
#         ('วิทยาลัยแพทยศาสตร์และการสาธารณสุข', 'วิทยาลัยแพทยศาสตร์และการสาธารณสุข'),
#         ('คณะนิติศาสตร์', 'คณะนิติศาสตร์'),
#         ('คณะรัฐศาสตร์', 'คณะรัฐศาสตร์'),
#         ('คณะพยาบาลศาสตร์', 'คณะพยาบาลศาสตร์'),
#     ]
#     faculty = forms.CharField(max_length=50, choices=faculty_choices, default="วิทยาศาสตร์")

#     class Meta:
#         model = UserStudent
#         fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name',  'address', 'phone']

class UserRecruitment_AnnouncerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='ชื่อ')  # เพิ่มชื่อ-สกุล
    last_name = forms.CharField(max_length=100, required=True, label='สกุล')  # สกุล
    address = forms.CharField(max_length=255, required=True, label='ที่อยู่')  # เพิ่มที่อยู่
    phone = forms.CharField(max_length=15, required=True, label='เบอร์โทรศัพท์')  # เพิ่มเบอร์โทรศัพท์

    class Meta:
        model = UserRecruitment_Announcer
        fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name', 'address', 'phone']
