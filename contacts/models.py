from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    phone=models.IntegerField(max_length=100)
    registrar=models.ForeignKey("Registrar",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.email}"
    
class Registrar(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username