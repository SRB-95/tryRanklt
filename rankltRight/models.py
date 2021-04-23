from django.db import models
# Create your models here.

class person(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.name
    