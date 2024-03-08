# Accounts/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import UserRecruitment_Announcer

# class UserFarmerBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = UserStudent.objects.get(username=username)
#         except UserStudent.DoesNotExist:
#             return None

#         if user.check_password(password):
#             user.backend = 'Accounts.backends.UserStudentBackend'  # Set the backend attribute
#             return user

#     def get_user(self, user_id):
#         try:
#             return UserStudent.objects.get(pk=user_id)
#         except UserStudent.DoesNotExist:
#             return None

class UserDriverBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserRecruitment_Announcer.objects.get(username=username)
        except UserRecruitment_Announcer.DoesNotExist:
            return None

        if user.check_password(password):
            user.backend = 'Accounts.backends.UserRecruitment_AnnouncerBackend'  # Set the backend attribute
            return user

    def get_user(self, user_id):
        try:
            return UserRecruitment_Announcer.objects.get(pk=user_id)
        except UserRecruitment_Announcer.DoesNotExist:
            return None
