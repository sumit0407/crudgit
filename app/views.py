from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def Index(request):
    return render(request,"app/index.html")

def index1(request):
    data=Admin.objects.all()
    return render(request,"app/index1.html",{'data':data})
    
def Data(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        passw=request.POST['passw']
        con=request.POST['con']
        if fname and lname and email and passw and con:
            a=Admin.objects.create(Firstname=fname,Lastname=lname,Email=email,Password=passw,Contact=con)
            return redirect("index1")

def updatedata(request,pk):
    i=Admin.objects.get(id=pk)
    return render(request,"app/update.html",{'i':i})
def Up(request,pk):
    x=Admin.objects.get(id=pk)
    x.Firstname=request.POST['fname'] if request.POST['fname'] else x.Firstname
    x.Lastname=request.POST['lname'] if request.POST['lname'] else x.Lastname
    x.Email=request.POST['email'] if request.POST['email'] else x.Email
    x.Password=request.POST['passw'] if request.POST['passw'] else x.Password
    x.Contact=request.POST['con'] if request.POST['con'] else x.Contact
    x.save()
    url=f"/updatedata/{pk}"
    return redirect(url)


def deleteddata(request,pk):
    a=Admin.objects.get(id=pk)
    a.delete()
    
    return redirect("index1")
