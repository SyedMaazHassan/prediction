from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your models here.

class countering(models.Model):
    which_user = models.ForeignKey(User, on_delete = models.CASCADE)
    code = models.CharField(max_length = 25)
    isEntered = models.BooleanField(default = False)

class predictions(models.Model):
    predicted_color = models.CharField(max_length = 7)
    actual_color = models.CharField(max_length = 7)
    status = models.BooleanField()
    reference_code = models.ForeignKey(countering, on_delete = models.CASCADE)

