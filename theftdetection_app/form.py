from django.forms import ModelForm
from .models import *
class Addpoliceform(ModelForm):
    class Meta:
        model=PoliceTable
        fields=['Name','phonenumber','email','location','pincode','telegram_id']