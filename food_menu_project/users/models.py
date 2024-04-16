from django.db import models

from django.contrib.auth.models import User #n built User model
# Create your models here.

#create user profile to display something about user
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE) # using User model to add some fields
    image=models.ImageField(default='picture_sagar.png',upload_to='profile_pictures')
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

#perform some shell operations
# python manage.py shell_plus --print-sql
# user=User.objects.filter(username='sagar').first()
# user
# user.profile
# user.profile.image