from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Titles(models.Model):
    title1 = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if Titles.objects.count() >= 1 and not self.pk:
            raise ValidationError("Only 1 records will be stored")
        super().save(*args, **kwargs)

class Section1(models.Model):
    t1h1 = models.CharField(max_length=50)
    t1sh1 = models.CharField(max_length=50)
    t1h2 = models.CharField(max_length=50)
    t1sh2 = models.CharField(max_length=50)
    t1h3 = models.CharField(max_length=50)
    t1sh3 = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if Section1.objects.count() >= 1 and not self.pk:
            raise ValidationError("Only 1 records are allowed in TableTwo.")
        super().save(*args, **kwargs)

class Section2(models.Model):
    a1 = models.CharField(max_length=120)
    a2 = models.CharField(max_length=120)
    a3 = models.CharField(max_length=120)
    a4 = models.CharField(max_length=120)
    a5 = models.CharField(max_length=120)