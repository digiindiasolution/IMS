from django.shortcuts import render,HttpResponse


# Create your views here.
def createBill_view(request):
    return render(request,"create-bill.html")