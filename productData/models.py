from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    price=models.IntegerField(null=True,blank=True)
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.name)



