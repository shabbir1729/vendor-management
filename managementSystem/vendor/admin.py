from django.contrib import admin
from .models import *


admin.site.site_header = 'VMS admin'
admin.site.site_title = 'VMS admin'
admin.site.index_title = 'Vendor Management administration'
admin.empty_value_display = '**Empty**'



@admin.register(Vendor)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name","vendor_code")
    list_filter = ("vendor_code",)
    search_fields = ("vendor_code",)


@admin.register(PurchaseOrder)
class UserAdmin(admin.ModelAdmin):
    list_display = ("po_number","vendor",)
    list_filter = ("po_number",)
    search_fields = ("po_number",)


@admin.register(HistoricalPerformance)
class UserAdmin(admin.ModelAdmin):
    list_display = ("vendor","quality_rating_avg",)
    list_filter = ("vendor",)
    search_fields = ("vendor",)

admin.site.register(User)