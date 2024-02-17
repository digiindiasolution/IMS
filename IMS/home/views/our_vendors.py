from django.shortcuts import render,HttpResponse


# Create your views here.
def ourVendors_view(request):
    return render(request,"our-vendors.html")