from django.shortcuts import render,HttpResponse


# Create your views here.
def allManufactureOrder(request):
    return render(request,"all-manufacture-order.html")