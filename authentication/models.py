from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


# Create your models here.

class CustomerUser(AbstractUser):
    telephone = models.CharField(max_length=15)
    groups = models.ManyToManyField(Group, related_name='user')
    user_permissions = models.ManyToManyField(Permission, related_name='users')

    ROLE_USER = 'user'
    ROLE_ADMIN = 'admin'

    ROLE_CHOICES = (
        (ROLE_USER, 'User'),
        (ROLE_ADMIN, 'Admin'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Role')
