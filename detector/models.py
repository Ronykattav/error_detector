from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class UserInput(models.Model):
    userId = models.IntegerField()
    problem = models.CharField(max_length=300)
    serialNum = models.CharField(max_length=64)
    onLights = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    offLights = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    blinkingLights = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)])
    date = models.DateTimeField(auto_now_add=True)
    msg = models.CharField(max_length=300, default="")

    # what to present in the admin page
    def __int__(self):
        return self.userId
