from django.shortcuts import render,HttpResponse


# Create your views here.
def addRowMaterial_view(request):
    return render(request,"add-raw-material.html")