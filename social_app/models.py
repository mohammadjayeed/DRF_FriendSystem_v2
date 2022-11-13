from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="friends", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user.user_name)
# STATUS_CHOICES = {

#     ('send','send'),
#     ('accepted','accepted'),
#     ('default','default')

# }

DEFAULT = 'default'
SEND = 'send'
ACCEPT = 'accepted'

STATUS_CHOICES = [
        (DEFAULT, 'default'),
        (SEND, 'send'),
        (ACCEPT, 'accepted'),
    ]
class Friendship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES ,default= DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.sender}'s request to {self.receiver}, status : {self.status}"



