from django.db import models
from django.contrib.auth.models import User

class Cronjob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    schedule = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class CronjobLog(models.Model):
    cronjob = models.ForeignKey(Cronjob, on_delete=models.CASCADE)
    execution_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    output = models.TextField()

    def __str__(self):
        return f"{self.cronjob.name} - {self.execution_time}"