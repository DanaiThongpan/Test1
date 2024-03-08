from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import migrations
# Create your models here.
# Accounts/models.py

def group_create(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    # Group.objects.create(name='student')
    Group.objects.create(name='recruitment_announcer')

class Migration(migrations.Migration):
    dependencies = [
        ('Accounts', 'previous_migration'),
    ]
    operations = [
        migrations.RunPython(group_create),
    ]

# class UserStudent(AbstractUser):
#     groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='Accounts_student_groups')
#     user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='Accounts_student_users_permissions')
#     id_student = models.IntegerField(primary_key=True)
#     username = models.TextField(max_length=20)
#     title_choices = [
#         ('นาย', 'นาย'),
#         ('นาง', 'นาง'),
#         ('นางนสาว', 'นางสาว'),
#     ]
#     title = models.CharField(max_length=10, choices=title_choices, default="วิทยาศาสตร์")
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.CharField(unique=True, max_length=30)
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
#     faculty = models.CharField(max_length=50, choices=faculty_choices, default="วิทยาศาสตร์")
#     def __str__(self):
#         return "student"   
#     @property
#     def is_student(self):
#         return True

#     @property
#     def is_recruitment_announcer(self):
#         return False

#     def __str__(self):
#         return 'student'

class UserRecruitment_Announcer(AbstractUser):
    groups = models.ManyToManyField(Group, verbose_name="Groups", blank=True, related_name='Accounts_recruitment_announcer_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name="User Permissions", blank=True, related_name='Accounts_recruitment_announcer_user_permissions')
    first_name = models.CharField(max_length=100, default='')  # เพิ่มชื่อ-สกุล
    last_name = models.CharField(max_length=100, default='')  # เพิ่มชื่อ-สกุล
    address = models.CharField(max_length=255, default='')  # เพิ่มที่อยู่
    phone = models.CharField(max_length=15, default='')  # เพิ่มเบอร์โทรศัพท์
    email = models.EmailField(max_length=255, unique=True)  # Keep email field only
    def __str__(self):
        return "recruitment_announcer"
    @property
    def is_student(self):
        return False

    @property
    def is_recruitment_announcer(self):
        return True

    def __str__(self):
        return 'recruitment_announcer'
