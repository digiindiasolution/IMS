from django.shortcuts import render,redirect
from django.contrib import messages
from home.models import add_vendor


# Create your views here.
def ourVendors_view(request):
    all_vendors=add_vendor.AddVendor.objects.all()
    return render(request,"our-vendors.html",{"all_vendors":all_vendors})

def addVendor_view(request):
    if request.method=="POST":
        vendor_name=request.POST.get('vendor_name')
        vendor_phone=request.POST.get('vendor_phone')
        contact_person=request.POST.get('contact_person')
        vendor_email=request.POST.get('vendor_email')
        vendor_gst=request.POST.get('vendor_gst')
        vendor_address=request.POST.get('vendor_address')
        try:
         
            checking_name=add_vendor.AddVendor.objects.filter(vendor_name=vendor_name)
            if len(checking_name) != 0 :
                print(checking_name)
                print('none ke andar aa gaya')
                messages.error(request , ' This Name is ALready Registerd')
                return redirect('/add-vendor')
            else:
                vendor_to_save=add_vendor.AddVendor(vendor_name=vendor_name,vendor_phone=vendor_phone,contact_person=contact_person,vendor_email=vendor_email,vendor_gst=vendor_gst,vendor_address=vendor_address)
                vendor_to_save.save()
                messages.success(request,'Vendor Aded Successfully')
                return redirect('/our-vendors')
                    
        except Exception as e:
            print(e)
            messages.error(request,'Something Went Wrong')
            return redirect('/add-vendor')
    return render(request,"add-vendor.html")

def deleteVendor_view(request,id):
    try:
        vendor_to_delete=add_vendor.AddVendor.objects.get(id=id)
        vendor_to_delete.delete()
        messages.success(request,'Vendor Deleted Successfully')
        return redirect('/our-vendors')
    except Exception as e:
        print(e)
        messages.error(request,'Something Went Wrong')
        return redirect('/our-vendors')

def updateVendor_view(request,id):
    vendor_to_update=add_vendor.AddVendor.objects.get(id=id)

    if request.method=="POST":
        vendor_name=request.POST.get('vendor_name')
        vendor_phone=request.POST.get('vendor_phone')
        contact_person=request.POST.get('contact_person')
        vendor_email=request.POST.get('vendor_email')
        vendor_gst=request.POST.get('vendor_gst')
        vendor_address=request.POST.get('vendor_address')

        try:

            vendor_to_update.vendor_name=vendor_name
            vendor_to_update.vendor_phone=vendor_phone
            vendor_to_update.contact_person=contact_person
            vendor_to_update.vendor_email=vendor_email
            vendor_to_update.vendor_gst=vendor_gst
            vendor_to_update.vendor_address=vendor_address
            vendor_to_update.save()
            messages.success(request,'Vendor Updated Successfully')
            return redirect('/our-vendors')
        except Exception as e:
            messages.error(request,'Something Went Wrong')
            return redirect('/update-vendor/{id}')
    return render(request,'update-vendor.html',{'vendor_to_update':vendor_to_update})