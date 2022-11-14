from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.conf import settings
from .models import *

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=Friendship)
def post_save_send_friend_request(sender, instance, created, **kwargs):
    
    invite_sender = instance.sender
    invite_receiver = instance.receiver
   

    if instance.status == "accepted":
        invite_sender.friends.add(invite_receiver.user)
        invite_receiver.friends.add(invite_sender.user)
        invite_sender.save()
        invite_receiver.save()
    
