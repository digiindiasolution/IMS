from django.shortcuts import render,redirect


# Create your views here.
def manufacturingOrder_view(request):
    return render(request,"add-manufacture-order.html")

def ourManufacurer_view(request):
    return render(request,'our-manufacturer.html')