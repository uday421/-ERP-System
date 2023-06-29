from django.contrib import admin

from .models import Challan, Received_Challan, Invoice, Received_Invoice, Received_Purchase_Order, Purchase_Order

# Register your models here.

admin.site.register(Challan)
admin.site.register(Received_Challan)
admin.site.register(Invoice)
admin.site.register(Received_Invoice)
admin.site.register(Received_Purchase_Order)
admin.site.register(Purchase_Order)