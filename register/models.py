from django.db import models

# Create your models here.

class user_registration(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    c_password = models.CharField(max_length=20)
    address = models.TextField(max_length=100)


    def __str__(self):
        return self.username
        
        

