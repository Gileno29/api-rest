from django.db import models
from  datetime import datetime
from django.utils import timezone
import uuid
# reate your models here.

class Item(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title=models.CharField(max_length=500)
    price=models.FloatField()
    description=models.TextField(max_length=500)
    created_on=models.DateTimeField(auto_now_add=True)
    type_item= models.CharField(max_length=255)
    estoque=models.ForeignKey("Estoque", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str(str(self.title) + ' ' + str(self.title) +  ' '+ str(self.price))

class Estoque(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name=models.CharField(max_length=50, null=False, default='Meu estoque')  
    create_on=models.DateTimeField(default=timezone.now)








