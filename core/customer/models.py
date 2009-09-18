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
        
class CustomerContact(models.Model):
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
        
class Customer(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ManyToManyField(CustomerContact)
    locations = models.ManyToManyField(Location)
    deleted = models.BooleanField(default=False)
    parent = models.ForeignKey('self')
    
    def __unicode__(self):
        return self.name
    
    def get_profile(self):
        """
        Returns site-specific profile for this Customer. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        if not hasattr(self, '_profile_cache'):
            from django.conf import settings
            if not getattr(settings, 'CUSTOMER_PROFILE_MODEL', False):
                raise SiteProfileNotAvailable
            try:
                app_label, model_name = settings.CUSTOMER_PROFILE_MODULE.split('.')
                model = models.get_model(app_label, model_name)
                self._profile_cache = model._default_manager.get(customer__id__exact=self.id)
                self._profile_cache.customer = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache
