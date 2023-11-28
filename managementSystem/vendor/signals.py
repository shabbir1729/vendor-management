from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from django.utils import timezone

from .models import *

# vendor/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg, Count
from django.utils import timezone
from .models import PurchaseOrder, Vendor, HistoricalPerformance

@receiver(post_save, sender=PurchaseOrder)
# @receiver(post_delete, sender=PurchaseOrder)
def calculate_performance_metrics(sender, instance, **kwargs):



    # Calculate On-Time Delivery Rate
    if instance.status == 'completed':
        completed_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
        on_time_delivered_pos = completed_pos.filter(delivery_date__lte=instance.delivery_date)
        on_time_delivery_rate = (on_time_delivered_pos.count() / completed_pos.count()) * 100
        instance.vendor.on_time_delivery_rate = on_time_delivery_rate

    # Calculate Quality Rating Average
    if instance.quality_rating is not None and instance.status == 'completed':
        quality_rating_avg = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed').aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
        instance.vendor.quality_rating_avg = quality_rating_avg

    # Calculate Average Response Time
    if instance.acknowledgement_date is not None:
        response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgement_date__isnull=False).values_list("acknowledgement_date", "issue_date")
        average_response_time = calculate_average_time_difference(response_times)
        instance.vendor.average_response_time = average_response_time

    # Calculate Fulfilment Rate
    total_pos = PurchaseOrder.objects.filter(vendor=instance.vendor)
    fulfilled_pos = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
    fulfillment_rate = (fulfilled_pos.count() / total_pos.count()) * 100 if total_pos.count() > 0 else 0.0
    instance.vendor.fulfillment_rate = fulfillment_rate

    instance.vendor.save()

@receiver(post_save, sender=Vendor)
def initialize_vendor_performance_metrics(sender, instance, created, **kwargs):
    if created:
        # Initialize vendor performance metrics for a new vendor
        HistoricalPerformance.objects.create(
            vendor=instance,
            date=timezone.now(),
            on_time_delivery_rate=instance.on_time_delivery_rate,
            quality_rating_avg=instance.quality_rating_avg,
            average_response_time=instance.average_response_time,
            fulfillment_rate=instance.fulfillment_rate
        )

def calculate_average_time_difference(time_tuples):
    if not time_tuples:
        return 0.0

    time_diff_sum = sum((end - start).total_seconds() for end, start in time_tuples)

    return time_diff_sum / len(time_tuples)



@receiver(post_save, sender=Vendor)
def set_vendor_code(sender, instance, created, **kwargs):

    if created:
        instance.vendor_code = "vm%04d" % instance.id
        instance.save()

@receiver(post_save, sender=PurchaseOrder)
def set_purchade_order_code(sender, instance, created, **kwargs):

    if created:
        instance.po_number = "po%04d" % instance.id
        instance.save()