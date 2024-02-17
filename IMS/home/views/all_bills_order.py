from django.shortcuts import render,HttpResponse


# Create your views here.
def allBillsOrder_view(request):
    return render(request,"all-bills-order.html")