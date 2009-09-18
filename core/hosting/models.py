from django.db import models
from django.forms import ModelForm

# Create your models here.

class CustomerProfile(models.Model):
    plan = models.CharField(max_length=50)
    
class CustomerProfileForm(ModelForm):
    class Meta(object):
        model = CustomerProfile

