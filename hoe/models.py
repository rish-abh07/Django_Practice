from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=130)
    email = models.CharField(max_length=130)
    suggestion = models.CharField(max_length=300)
    def __str__(self):
        return self.name