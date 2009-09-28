from django.db import models

# Create your models here.

class Account(models.Model):
    customer_id = models.CharField(max_length=25, db_index=True)
    account_number = models.CharField(max_length=25)
    
class PaymentInfoType(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    
class PaymentInfo(models.Model):
    type = models.ForeignKey(PaymentInfoType)
    account_number = models.CharField(max_length=255)
    routing_number = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    expiration = models.DateField(null=True)
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=10)
    account = models.ForeignKey(Account)
    
class Invoice(models.Model):
    account = models.ForeignKey(Account)
    number = models.CharField(max_length=20)
    inv_date = models.DateField()
    due_date = models.DateField()
    paid_time = models.DateTimeField(null=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=5)
    postal_code = models.CharField(max_length=10)
    from_address = models.CharField(max_length=50)
    from_address2 = models.CharField(max_length=50)
    from_city = models.CharField(max_length=50)
    from_state_province = models.CharField(max_length=5)
    from_postal_code = models.CharField(max_length=10)
    
class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice)
    qty = models.IntegerField()
    desc = models.CharField(max_length=255)
    itm_amount = models.DecimalField(max_digits=8, decimal_places=2)
    line_amount = models.DecimalField(max_digits=8, decimal_places=2)
    
class Payment(models.Model):
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account)
    
class InvoicePayment(models.Model):
    invoice = models.ForeignKey(Invoice)
    payment = models.ForeignKey(Payment)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    