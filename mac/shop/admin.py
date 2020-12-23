from django.contrib import admin

# Register your models here.
from .models import product , Contact,Order,login,register
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(register)
admin.site.register(login)