from django.forms import ModelForm
from .models import *

class Addpoliceform(ModelForm):
    class Meta:
        model=PoliceTable
        fields=['Name','phonenumber','email','location','pincode','telegram_id']


class Addcriminalsform(ModelForm):
    class Meta:
        model=CriminalsTable
        fields=['Name','photo','phonenumber','email','id_proof','Address','category_of_crime','previous_cases']

