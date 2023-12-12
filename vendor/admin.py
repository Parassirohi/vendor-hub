from django.contrib import admin
from .models import Vendor, PurchaseOrder, HistoricalPerformance

admin.site.register(Vendor,PurchaseOrder, HistoricalPerformance)
