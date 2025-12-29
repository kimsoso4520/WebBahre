from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    # فیلدهای اضافی
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_staff_member = models.BooleanField(default=False)  # نقش سازمانی
    personel_code = models.CharField(max_length=15, blank=True, null=False)
    # می‌تونی فیلدهای دیگه هم اضافه کنی

    def __str__(self):
        return self.username
