from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given username, email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        
        user.save(using=self._db)     
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):

    USERNAME_FIELD = 'email'
    username        = None

    email           = models.EmailField(max_length=50, unique=True)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    address         =  models.TextField(blank=True)
    PHONE_REGEX     = RegexValidator(r'^\+?1?\d{9,15}$', "Phone number must be entered in the format: '+9999999999'. Up to 15 digits allowed.")
    phone           = models.CharField(max_length=15, blank=True,validators=[PHONE_REGEX])
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=True)


    objects = MyUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Vendor(models.Model):

    name                    = models.CharField(max_length=30,null=False,blank=False)
    contact_details         = models.TextField(null=False,blank=False)
    address                 = models.TextField(null=False,blank=False)
    vendor_code             = models.CharField(max_length=30,null=True,blank=True)
    on_time_delivery_rate   = models.FloatField(blank=True, null=True, default=0)
    quality_rating_avg      = models.FloatField(blank=True, null=True, default=0)
    average_response_time   = models.FloatField(blank=True, null=True, default=0)
    fulfillment_rate        = models.FloatField(blank=True, null=True, default=0)

    created_at              = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at              = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "All Vendors"
    
    def __str__(self):
        return self.name


po_status = (
    ('pending','pending'),
    ('completed','completed'),
    ('cancelled','cancelled')
    )


class PurchaseOrder(models.Model):

    po_number               = models.CharField(max_length=20,blank=True, null=True)
    vendor                  = models.ForeignKey(Vendor,on_delete=models.CASCADE,related_name="fk_vendor_po")
    order_date              = models.DateTimeField()
    delivery_date           = models.DateTimeField()
    items                   = models.JSONField(blank=True, null=True)
    quantity                = models.IntegerField(blank=True, null=True, default=0)
    status                  = models.CharField(choices=po_status,default='pending', blank=False,max_length=20)
    quality_rating          = models.FloatField(blank=True, null=True, default=0)
    issue_date              = models.DateTimeField()
    acknowledgement_date    = models.DateTimeField(blank=True, null=True)

    created_at              = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at              = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "All Purchase Orders"
    
    def __str__(self):
        return self.po_number


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
        verbose_name = "Vendor Performance"
        verbose_name_plural = "All Vendor Performances"
    
    def __str__(self):
        return self.vendor.name