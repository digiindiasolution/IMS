from django.shortcuts import render,HttpResponse


# Create your views here.
def manufacturingOrder_view(request):
    return render(request,"add-manufacture-order.html")