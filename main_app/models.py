from django.db import models


class PremisesState(models.TextChoices):
    DISARMED = 'DISARMED'
    GUARDED = 'GUARDED'
    ALARM = 'ALARM'


class Premises(models.Model):
    address = models.CharField(max_length=100, unique=True)
    state = models.CharField(max_length=50,
                             choices=PremisesState.choices,
                             default=PremisesState.DISARMED)

    def __str__(self) -> str:
        return self.address
