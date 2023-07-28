from django.db import models
from django.contrib.auth.models import User


class SignUpModel(models.Model):
     first_name=models.CharField(max_length=40)
     last_name=models.CharField(max_length=40)
     email=models.EmailField()
     phone_number=models.CharField(max_length=40)

     def __str__(self):
          return self.first_name

     class Meta:
          db_table='new_users'



#     title=models.CharField(max_length=50)
#     body=models.TextField(null=True, blank=True)
#     image=models.ImageField(null=True, blank=True, upload_to='post_images')
#     author=models.ForeignKey(User)
# Create your models here.
