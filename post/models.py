from django.db import models

from django.utils import timezone

objects = models.Manager()

class Orders(models.Model):
    user = models.CharField(max_length=100,null = True)
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    price = models.IntegerField(null=True)
    puplished = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20,null=True)

    
    def __str__(self):
        return self.title
    
class Loginfo(models.Model):
    username = models.CharField(max_length=50,null = True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username