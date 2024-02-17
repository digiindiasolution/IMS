from django.shortcuts import render,HttpResponse


# Create your views here.
def semiFinishedGoods_view(request):
    return render(request,"semi-finished-goods.html")
