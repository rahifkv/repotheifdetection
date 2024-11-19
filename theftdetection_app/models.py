from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)

class PoliceTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    phonenumber = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=40,  blank=True, null=True)
    pincode = models.IntegerField( blank=True, null=True)
    telegram_id=models.CharField(max_length=100,null=True,blank=True)


class CategoryTable(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)

class CriminalsTable(models.Model):
    POLICESTATION = models.ForeignKey(PoliceTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    phonenumber = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    id_proof = models.CharField(max_length=20, blank=True, null=True)
    Address = models.CharField(max_length=30, blank=True, null=True)
    category_of_crime =models.CharField(max_length=20, blank=True, null=True)
    previous_cases =models.CharField(max_length=20, blank=True, null=True)

class UserTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True, null=True)
    user_id = models.BigIntegerField( blank=True, null=True)
    phonenumber = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
    house_name = models.CharField(max_length=20, blank=True, null=True)
    place = models.CharField(max_length=15, blank=True, null=True)
    pincode = models.BigIntegerField( blank=True, null=True)
    post =  models.CharField(max_length=15, blank=True, null=True)

class NotificationTable(models.Model):
    date = models.DateTimeField( blank=True, null=True)
    notification = models.CharField( max_length=30,blank=True,null=True)

    