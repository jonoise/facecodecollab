from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserModel
from account.models import Account

@receiver(post_save, sender=UserModel)
def UserAccount(sender, instance, created, **kwargs):
    if created:
        Account(user=instance)
        instance.account.save()