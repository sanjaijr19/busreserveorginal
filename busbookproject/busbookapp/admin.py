from django.contrib import admin
from .models import User,MyModel

# Register your models here.
from django.contrib import admin
from busbookapp.models import Driver,Customer
class DriverAdmin(admin.ModelAdmin):
    driverdetails=["drivername","age","contact_no","bus_no"]


class CustomerAdmin(admin.ModelAdmin):
    consumerdetail=["name","age","address","phone","start","end","date","time"]

class UserAdmin(admin.ModelAdmin):
    Userdetails=['is_admin','is_customer','is_driver']

admin.site.register(Driver,DriverAdmin)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(MyModel)

# Register your models here.

# Register your models here.
