from django.contrib import admin

# Register your models here.
from .models import Lender, Product

admin.site.register(Lender)
admin.site.register(Product)