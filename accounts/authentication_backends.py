from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

class EidBackend(BaseBackend):
    def authenticate(self, request, eid=None, password=None):
        try:
            # Fetch user based on eid
            user_profile = UserProfile.objects.get(eid=eid)
            user = user_profile.user
            if user.check_password(password):
                return user
        except UserProfile.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
