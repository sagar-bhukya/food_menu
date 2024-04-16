from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.
class Item(models.Model):

    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)# it is going add username who is upload the post
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=1000,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTGGTA9HaRdJ061vUclkH21iUOcK-Fn4oJAg&s")

    def __str__(self):
        return self.item_name
    #whenevev the creates an item we want djnago to redirect us to the detailed view of specific item 
    def get_absolute_url(self):#Redirecting users to the detail page of an instance right after creating or editing it in forms or views.
        return reverse("detail", kwargs={"pk": self.pk})
    
    

#python manage.py sqlmigrate food 0001 : gives the sql query
'''BEGIN;
--
-- Create model Item
--
CREATE TABLE "food_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "item_name" varchar(200) NOT NULL, "item_desc" varchar(200) NOT NULL, "item_price" integer NOT NULL);
COMMIT;'''


#Adding data to the table Item so we have to interactive with the python shell

#a.id and a.pk: gives unique id