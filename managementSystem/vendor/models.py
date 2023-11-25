from django.db import models


class Vendor(models.Model):

    name                    = models.CharField(max_length=30,null=False,blank=False)
    contact_details         = models.TextField(null=False,blank=False)
    address                 = models.TextField(null=False,blank=False)
    vendor_code             = models.CharField()
    on_time_delivery_rate   = models.FloatField()
    quality_rating_avg      = models.FloatField()
    average_response_time   = models.FloatField()
    fulfillment_rate        = models.FloatField()

    created_at              = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at              = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Vendor"
        verbose_name_plural = "All Vendors"
    
    def __str__(self):
        return self.name

    def generate_vendor_code(self):
        return f"vms{self.id}"
    
    def save(self,*arg,**kwarg):
        self.vendor_code = self.generate_vendor_code()
        super().save(*arg,**kwarg)
    


po_status = (
    ('pending','pending'),
    ('completed','completed'),
    ('cancelled','cancelled')
    )


class PurchaseOrder(models.Model):

    po_number               = models.CharField()
    vendor                  = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name="fk_vendor_po")
    order_date              = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    delivery_date           = models.DateTimeField()
    items                   = models.JSONField()
    quantity                = models.IntegerField()
    status                  = models.CharField(choices=po_status,default='pending', blank=False)
    quality_rating          = models.FloatField(null=True)
    issue_date              = models.DateTimeField()
    acknowledgement_date    = models.DateTimeField(null=True)

    created_at              = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at              = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Purchase Order"
        verbose_name_plural = "All Purchase Orders"
    
    def __str__(self):
        return self.po_number

    def generate_po_code(self):
        return f"po{self.id}"
    
    def save(self,*arg,**kwarg):
        self.po_number = self.generate_po_code()
        super().save(*arg,**kwarg)


class HistoricalPerformance(models.Model):

    vendor                  = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="fk_vendor_history")
    date                    = models.DateTimeField()
    on_time_delivery_rate   = models.FloatField()
    quality_rating_avg      = models.FloatField()
    average_response_time   = models.FloatField()
    fulfillment_rate        = models.FloatField()

    created_at              = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at              = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Vendor Performance"
        verbose_name_plural = "All Vendor Performances"
    
    def __str__(self):
        return self.vendor