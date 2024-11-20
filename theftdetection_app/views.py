from urllib import request
from django.shortcuts import render,redirect
from django.views import View
from .form import *
from .models import *


# Create your views here.

class Loginpage(View):
    def get(self,request):
        return render(request,"administration/login.html")
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=LoginTable.objects.get(username=username,password=password)
        if login_obj.type=='admin':
            return render(request,'administration/admindashboard.html')
    
class AddCriminals(View):
    def get(self,request):
        obj=PoliceTable.objects.all()
        return render(request,"administration/add criminals.html",{'val':obj})
    def post(self,request):
        form=Addcriminalsform(request.POST, request.FILES)
        if form.is_valid():
            f=form.save(commit=False)
            f.POLICESTATION = PoliceTable.objects.get(id=request.POST['police_id'])
            f.save()
            return render(request,'administration/admindashboard.html')




class AddPoliceStation(View):
    def get(self,request):
        return render(request,"administration/add police station.html")
    def post(self,request):
        form=Addpoliceform(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            username = request.POST['username']
            password = request.POST['password']
            obj = LoginTable()
            obj.username = username
            obj.password = password
            obj.type = "police"
            obj.save()
            f.LOGIN=obj
            f.save()
            return redirect('viewpolicestation')
    
class ViewCriminals(View):
    def get(self,request):
        obj = CriminalsTable.objects.all()
        return render(request,"administration/view criminals.html", {'val': obj})
    
class ViewDetectionDetails(View):
    def get(self,request):
        return render(request,"administration/view detection details.html")
    
class ViewPoliceStation(View):
    def get(self,request):
        obj = PoliceTable.objects.all()
        return render(request,"administration/view police station.html", {'val': obj})

class EditPolice(View):
    def get(self,request, police_id):
        obj = PoliceTable.objects.get(id=police_id)
        return render(request,"administration/edit police station.html",{'val': obj} )
    def post(self,request, police_id):
        obj = PoliceTable.objects.get(id=police_id)
        form=Addpoliceform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('viewpolicestation')

class deletepolice(View):
    def get(self,request, police_id):
        obj = LoginTable.objects.get(id=police_id)
        obj.delete()
        return redirect('viewpolicestation')
        



class ViewUser(View):
    def get(self,request):
         obj = UserTable.objects.all()
         return render(request,"administration/view user.html", {'val': obj})

class AdminHome(View):
    def get(self,request):
        return render(request,"administration/admindashboard.html")
