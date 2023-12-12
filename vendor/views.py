
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

class VendorViewSet(ModelViewSet):
    queryset = Vendor.objects.all
    serializer_class = VendorSerializer
    
class PurchaseOrderViewSet(ModelViewSet):
    queryset = PurchaseOrder.objects.all
    serializer_class = PurchaseOrderSerializer
    
class HistoricalPerformanceViewSet(ModelViewSet):
    queryset = HistoricalPerformance.objects.all
    serializer_class = HistoricalPerformanceSerializer
