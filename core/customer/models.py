from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Location(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    
    def __unicode__(self):
        return "%s\n%s, %s %s" % \
            (self.address, self.city, self.state, self.postal_code)
        
class BusinessContact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    location = models.ForeignKey(Location)
    user = models.ForeignKey(User, unique=True, null=True, blank=True)
    
    def __unicode__(self):
        if self.user:
            return "%s - %s %s" % \
                (self.user.username, self.user.first_name, self.user.last_name)
        else:
            return "%s %s" % (self.first_name, self.last_name)
        
class Business(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ManyToManyField(BusinessContact)
    locations = models.ManyToManyField(Location)
    parent = models.ForeignKey('self')
    
    def __unicode__(self):
        return self.name
    
