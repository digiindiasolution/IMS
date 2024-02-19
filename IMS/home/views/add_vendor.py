from django.shortcuts import render,HttpResponse


# Create your views here.
def addVendor_view(request):
    return render(request,"add-vendor.html")