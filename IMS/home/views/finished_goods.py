from django.shortcuts import render,HttpResponse


# Create your views here.
def finisedGoods_view(request):
    return render(request,"finished-goods.html")
