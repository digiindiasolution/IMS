from django.db import models

class AddVendor(models.Model):
    vendor_name=models.CharField(max_length=254,null=True,blank=True)
    vendor_phone=models.CharField(max_length=30,null=True,blank=True)
    contact_person=models.CharField(max_length=100,null=True,blank=True)
    vendor_email=models.EmailField(max_length=200,null=True,blank=True)
    vendor_gst=models.CharField(max_length=100,null=True,blank=True)
    vendor_address=models.CharField(max_length=300,null=True,blank=True)

    def __str__(self) -> str:
        return self.vendor_name