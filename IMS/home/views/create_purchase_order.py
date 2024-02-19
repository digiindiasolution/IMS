from django.shortcuts import render,HttpResponse


# Create your views here.
def createPurchaseOrder_view(request):
    return render(request,"create-purchase-order.html")