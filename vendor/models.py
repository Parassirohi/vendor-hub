from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_detail = models.TextField(null=True, blank=True)
    adderss = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=255, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    ORDER_STATUS_PENDING = 'P'
    ORDER_STATUS_COMPLETE = 'C'
    ORDER_STATUS_FAILED = 'F'
    ORDER_STATUS_CHOICES = [
        (ORDER_STATUS_PENDING, 'Pending'),
        (ORDER_STATUS_COMPLETE, 'Complete'),
        (ORDER_STATUS_FAILED, 'Failed')
    ]
    
    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)
    items = models.JSONField()
    quantity = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=255, status= ORDER_STATUS_CHOICES, default= ORDER_STATUS_PENDING)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"PurchaseOrder {self.po_number}"
    
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return f"HistoricalPerformance for {self.vendor} on {self.date}"

    
    
    
