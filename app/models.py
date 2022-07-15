from django.db import models

# Create your models here.
class School(models.Model):
    Sid=models.PositiveIntegerField(primary_key=True)
    Sname=models.CharField(max_length=100)


    def __str__(self):
        return self.Sname