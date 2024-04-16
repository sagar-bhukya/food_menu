from django.db.models.signals import post_save #use post save beacuase we want to get signal when the user data is saved or when the user is actually register
from django.dispatch import receiver # reciever will do is that it will recieve the send signal and it will perform some actions. ac
from django.contrib.auth.models import User

from .models import Profile

#write to function to build a profile
@receiver(post_save,sender=User)
def build_profile(sender,instance, created,**kwargs):  # sender is send the signal and instance is user being saved. instance from register when form is saved this isna
                                  # created which is gives boolean value if user created or not status of the user
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
