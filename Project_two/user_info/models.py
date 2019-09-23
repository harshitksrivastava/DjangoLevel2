from django.db import models

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length =50)
    Last_name = models.CharField(max_length = 50)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return str(self.First_name)+" "+str(self.Last_name)
