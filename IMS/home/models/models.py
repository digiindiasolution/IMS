from django.db import models


class Unit(models.Model):
    unit=models.CharField(max_length=100,unique=True,null=False,blank=False)

    def __str__(self) -> str:
        return self.unit

