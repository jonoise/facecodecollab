from django.db import models
from languages.models import Language, Framework
from users.models import UserModel

class Account(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='account')
    dob = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    language = models.ManyToManyField(Language, blank=True, related_name="account")
    framework = models.ManyToManyField(Framework, blank=True, related_name="account")
    is_active = models.BooleanField(default=True)
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} account'.capitalize()