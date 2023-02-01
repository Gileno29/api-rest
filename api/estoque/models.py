from django.db import models

# reate your models here.

class Itens(models.Model):
    title=models.CharFild(max_legth=255)
    value=models.FloatField()

