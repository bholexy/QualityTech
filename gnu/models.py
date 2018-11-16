from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class CustomUser(AbstractUser):
#     username = models.CharField(blank=True, max_length=255) 
#     first_name = models.CharField(('First Name of User'), blank = True, max_length = 20)
#     last_name = models.CharField(('Last Name of User'), blank = True, max_length = 20) 		

#     def __str__(self):
#         return self.username
