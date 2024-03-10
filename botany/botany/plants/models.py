from django.db import models

class Add(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.IntegerField()
    def __str__(self):
        return self.name
# Create your models here.
