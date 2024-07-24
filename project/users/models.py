from django.db import models

class UserModel(models.Model):
    first_name=models.CharField( max_length=50,blank=False,default='')
    last_name=models.CharField( max_length=50,blank=False,default='')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def str(self):
        return self.username