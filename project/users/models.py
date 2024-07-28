from django.db import models

class UserModel(models.Model):
    first_name=models.CharField( max_length=50,blank=False,default='')
    last_name=models.CharField( max_length=50,blank=False,default='')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username