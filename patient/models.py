import email
from django.db import models

# Create your models here.
class Patient(models.Model):

    Gender=(
        ('M', 'M'),
        ('F','F'),
    )


    name=models.CharField(max_length=40)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    age=models.CharField(max_length=3)
    gender=models.CharField(max_length=1, null=True,choices=Gender)
    note=models.TextField()
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name