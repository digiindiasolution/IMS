from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

from home.models.models import Unit
from home.models import add_vendor,raw_material

def rawMaterial_view(request):
    material_data=raw_material.AddRawMaterial.objects.all()
    return render(request,"raw-materials.html",{'material_data':material_data})


def addRowMaterial_view(request):
    units=Unit.objects.all()
    all_vendors=add_vendor.AddVendor.objects.all()

    if request.method == "POST":
        try: 
            vendor_name=add_vendor.AddVendor.objects.get(vendor_name=request.POST.get('vendor_name'))
            material_name=request.POST.get('material_name')
            quantity=request.POST.get('quantity')
            unit=request.POST.get('unit')
            # category=request.POST.get('category')
            checking_material=raw_material.AddRawMaterial.objects.filter(rawmaterial_name=material_name)
            if len(checking_material) != 0:
                check_to_save=checking_material[0]
                check_to_save.quantity += int(quantity)
                check_to_save.save()
            else:
                material_to_add=raw_material.AddRawMaterial(vendor_name=vendor_name,rawmaterial_name=material_name,quantity=quantity,unit=unit)
                material_to_add.save()
            history_to_create=raw_material.MaterialHistory(vendor_name=vendor_name,rawmaterial_name=material_name,quantity=quantity,unit=unit)
            history_to_create.save()
            messages.success(request,'Material Aded Successfully')
            return redirect('/add-raw-material')

        except Exception as e:
            print(e)
            print('exception men aa gaya')
            messages.error(request,'Something Went Wrong')
            return redirect('/raw-materials')
    return render(request,"add-raw-material.html",{'units':units,'all_vendors':all_vendors})

def materialHistory_view(request,vendor):
    try:
        vendor_to_get=add_vendor.AddVendor.objects.get(vendor_name=vendor)
        print(vendor_to_get,'is gated vendor')
        vendor_history=raw_material.MaterialHistory.objects.filter(vendor_name=vendor_to_get)
        return render(request,'material-history.html',{"vendor_history":vendor_history,'vendor_to_get':vendor_to_get})
    except Exception as e:
        messages.error(request,'Something Went Wrong')
        return redirect('/our-vendors')
