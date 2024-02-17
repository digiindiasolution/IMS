from django.shortcuts import render,HttpResponse


# Create your views here.
def allPurchaseOrder_views(request):
    return render(request,"all-purchase-order.html")