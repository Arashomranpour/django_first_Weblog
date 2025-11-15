from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nationalcode=models.PositiveIntegerField()
    image=models.ImageField(upload_to="profiles/images",blank=True,null=True,default="images/default-avatar.png")
    def __str__(self):
        return self.user.username
    