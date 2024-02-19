from django.contrib import admin

# Register your models here.
from home.models import add_vendor

class AdminAddvendor(admin.ModelAdmin):
    list_display=('id','vendor_name','vendor_phone','contact_person','vendor_email','vendor_gst','vendor_address')
    

admin.site.register(add_vendor.AddVendor,AdminAddvendor)


