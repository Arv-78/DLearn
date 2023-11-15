from django.db import models

# Create your models here.
class Contact(models.Model):
    name =  models.CharField(max_length=112)
    surname = models.CharField(max_length=112)
    username = models.CharField(max_length=112)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)

    def __str__(self):
        return self.name