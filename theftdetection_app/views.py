from urllib import request
from django.shortcuts import render,redirect
from django.views import View
from .form import *


# Create your views here.

class Loginpage(View):
    def get(self,request):
        return render(request,"administration/login.html")
    def post(self,reques):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=logintable.objects.get(username=username,password=password)
        if login_obj.type=='admin':
            return render(request,'administration/admindashboard.html')
    
class AddCriminals(View):
    def get(self,request):
        return render(request,"administration/add criminals.html")
    

class AddPoliceStation(View):
    def get(self,request):
        return render(request,"administration/add police station.html")
    def post(self,request):
        form=Addpoliceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewpolicestation')
    
class ViewCriminals(View):
    def get(self,request):
        return render(request,"administration/view criminals.html")
    
class ViewDetectionDetails(View):
    def get(self,request):
        return render(request,"administration/view detection details.html")
    
class ViewPoliceStation(View):
    def get(self,request):
        return render(request,"administration/view police station.html")
    
class ViewUser(View):
    def get(self,request):
        return render(request,"administration/view user.html")

class AdminHome(View):
    def get(self,request):
        return render(request,"administration/admindashboard.html")
