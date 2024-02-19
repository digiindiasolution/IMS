from django.shortcuts import render,HttpResponse


# Create your views here.
def addMember_view(request):
    return render(request,"add-members.html")