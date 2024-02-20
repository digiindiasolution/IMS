from django.db import models
from home.models.add_vendor import AddVendor
from home.models.models import *


class AddRawMaterial(models.Model):
    vendor_name=models.ForeignKey(AddVendor,on_delete=models.CASCADE)
    rawmaterial_name=models.CharField(max_length=254,null=False,blank=False)
    quantity=models.PositiveIntegerField(null=True,blank=True)
    unit=models.CharField(max_length=150)
    # category=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.rawmaterial_name



class MaterialHistory(models.Model):
    vendor_name=models.ForeignKey(AddVendor,on_delete=models.CASCADE)
    rawmaterial_name=models.CharField(max_length=254,null=False,blank=False)
    quantity=models.PositiveIntegerField(null=True,blank=True)
    unit=models.CharField(max_length=150)
    timestamp=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.rawmaterial_name


