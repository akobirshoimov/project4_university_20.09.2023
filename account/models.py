from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UniversityUser(AbstractUser):
    CHOICE_ROLES = (
        (3,'director'),
        (2,'teacher'),
        (1,'student')
    )

    roles = models.IntegerField(choices=CHOICE_ROLES,default=2)

    
