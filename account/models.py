from django.db import models
from languages.models import Language
from users.models import UserModel

class Account(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='account')
    dob = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True, related_name="accounts")