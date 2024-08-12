from django.db import models

# Create your models here.

class Tutor(models.Model):
    mode = models.CharField(max_length=70)
    classhour = models.DecimalField(decimal_places=2, max_digits=10)
    classdate = models.DateField()

