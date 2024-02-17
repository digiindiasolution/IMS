from django.shortcuts import render,HttpResponse


# Create your views here.
def ourMembers_view(request):
    return render(request,"our-members.html")