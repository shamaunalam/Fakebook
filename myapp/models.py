from django.db import models
from django.contrib.auth.models import User
# Create your models here
class User_Profile(models.Model):

    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    status = models.TextField(max_length=300,blank=True,default = 'Hey There I am on fakebook')
    location = models.CharField(max_length=100,blank=True)
    pic = models.ImageField(upload_to='media',blank=True)

    def __str__(self):
        return self.user.username
    


