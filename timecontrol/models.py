from django.db import models
from users.models import User


class Timecontrol(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
    time = models.CharField(max_length=5, blank=True, null=True)
    flaw = models.CharField(max_length=5, blank=True, null=True)
