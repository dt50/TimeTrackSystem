from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "m", "Мужчина"
        FEMALE = "f", "Женщина"

    class Dismissed(models.IntegerChoices):
        DISMISSED = 1, "Уволен"
        NOTDISMISSED = 2, "Не уволен"

    class BOSS(models.IntegerChoices):
        BOSS = 1, "Начальство"
        EMPLOYEE = 2, "Сотрудник"

    id_user = models.IntegerField("ID пользователя", null=True, blank=True)
    middle_name = models.CharField("Отчество", max_length=150, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, choices=Gender.choices)
    card = models.IntegerField("ID персональной карты", null=True, blank=True)
    dismissed = models.IntegerField(
        "Статус увольнения",
        null=True,
        choices=Dismissed.choices,
        default=Dismissed.NOTDISMISSED,
    )
    admin = models.BooleanField("Администратор", null=True, blank=True)
    boss = models.IntegerField(
        "Статус начальства",
        null=True,
        choices=BOSS.choices,
        default=BOSS.EMPLOYEE,
        blank=True,
    )
