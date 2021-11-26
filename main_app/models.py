from django.db import models


class Premises(models.Model):
    address = models.CharField(max_length=100, unique=True)
    guarded = models.BooleanField(default=False)
    alarm = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.address

    def arm(self):
        self.guarded = True

    def disarm(self):
        self.guarded = False
