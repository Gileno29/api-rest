from django.db import models
import uuid
# reate your models here.



class Item(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title=models.CharFild(max_legth=255)
    price=models.FloatField()
    description=models.TextField(max_length=500)
    created_on=models.DateTimeField(auto_now_add=True)
    estoque=models.ForeignKey()

class estoque(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    





