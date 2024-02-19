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
            category=request.POST.get('category')
            checking_material=raw_material.AddRawMaterial.objects.filter(rawmaterial_name=material_name)
            if len(checking_material) != 0:
                check_to_save=checking_material[0]
                check_to_save.quantity += int(quantity)
                check_to_save.save()
            else:
                material_to_add=raw_material.AddRawMaterial(vendor_name=vendor_name,rawmaterial_name=material_name,quantity=quantity,unit=unit,category=category)
                material_to_add.save()
            history_to_create=raw_material.MaterialHistory(vendor_name=vendor_name,rawmaterial_name=material_name,quantity=quantity,unit=unit,category=category)
            history_to_create.save()
            messages.success(request,'Material Aded Successfully')
            return redirect('/raw-materials')

        except Exception as e:
            print(e)
            print('exception men aa gaya')
            messages.error(request,'Something Went Wrong')
            return redirect('/raw-materials')
    return render(request,"add-raw-material.html",{'units':units,'all_vendors':all_vendors})