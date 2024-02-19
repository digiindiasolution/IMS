from django.shortcuts import render,HttpResponse


# Create your views here.
def addFinishedGoods_view(request):
    return render(request,"add-finished-goods.html")