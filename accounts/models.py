import uuid
from django.db import models
from django.contrib.auth.models import User

# Define user roles
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('HR', 'HR'),
    ('Employee', 'Employee'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    eid = models.CharField(max_length=10, unique=True, editable=False, default='')

    def save(self, *args, **kwargs):
        if not self.eid:
            # Generate a unique ID using UUID and limit it to the first 10 characters
            self.eid = str(uuid.uuid4().hex[:10]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.user} : {self.eid}"


# Role-specific models
class AdminProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"HR Profile for {self.user_profile}"


class HRProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"HR Profile for {self.user_profile}"




class EmployeeProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_profile.user.username} ({self.user_profile.role}) - {self.user_profile.eid}"
