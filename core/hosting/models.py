from django.db import models
from django.forms import ModelForm
from customer.models import Customer

# Create your models here.

class CustomerProfile(models.Model):
    plan = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, null=True, unique=True)
    
class CustomerProfileForm(ModelForm):
    class Meta(object):
        model = CustomerProfile
        exclude = ('customer',)
