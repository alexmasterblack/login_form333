from django.db import models


# Create your models here.

class User(models.Model):
    gender = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.second_name
