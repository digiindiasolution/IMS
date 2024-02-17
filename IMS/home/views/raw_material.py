from django.shortcuts import render,HttpResponse

def rawMaterial_view(request):
    return render(request,"raw-materials.html")