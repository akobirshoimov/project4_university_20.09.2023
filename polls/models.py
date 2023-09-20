from django.db import models
from datetime import datetime

# Create your models here.
class UniversityModel(models.Model):
    name = models.CharField(max_length=150)
    build_in = models.DateTimeField(default=datetime.now)
    is_old = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.name
    
