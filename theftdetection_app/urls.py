from ast import Name
from django.contrib import admin
from django.urls import path

from theftdetection_app.views import *
urlpatterns = [
    path('',Loginpage.as_view(),name="login"),
    path('addcriminals',AddCriminals.as_view(),name="addcriminals"),
    path('addpolicestation',AddPoliceStation.as_view(),name="addpolicestation"),
    path('viewcriminals',ViewCriminals.as_view(),name="viewcriminals"),
    path('viewdetectiondetails',ViewDetectionDetails.as_view(),name="viewdetectiondetails"),
    path('viewpolicestation',ViewPoliceStation.as_view(),name="viewpolicestation"),
    path('edit_police/<int:police_id>',EditPolice.as_view(),name="edit_police"),
    path('delete_police/<int:police_id>',deletepolice.as_view(),name="delete_police"),
    path('delete_criminals/<int:criminal_id>',deletecriminals.as_view(),name="delete_criminals"),
    path('viewuser',ViewUser.as_view(),name="viewuser"),
    path('adminhome',AdminHome.as_view(),name="adminhome"),

]

