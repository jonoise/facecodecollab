from django.db import models
from languages.models import Language, Framework
from users.models import UserModel

class Account(models.Model):
    # GENERAL
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='account')
    dob = models.DateField(verbose_name='Fecha de nacimiento', blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True, related_name="account")
    frameworks = models.ManyToManyField(Framework, blank=True, related_name="account")
    # SOCIAL
    github = models.URLField(verbose_name='github', blank=True, null=True)
    # ACCOUNT STATUS
    is_active = models.BooleanField(default=True)
    is_tutor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} account'.capitalize()