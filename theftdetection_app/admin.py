from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(LoginTable)

admin.site.register(PoliceTable)

admin.site.register(CategoryTable)

admin.site.register(CriminalsTable)

admin.site.register(UserTable)

admin.site.register(NotificationTable)
