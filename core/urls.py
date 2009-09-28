from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^core/', include('core.foo.urls')),
    (r'^customers/', include('customer.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    
    ####################### AUTH URLS #################
    (r'^accounts/login', 'django.contrib.auth.views.login'),
    (r'^accounts/logout', 'django.contrib.auth.views.logout'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        ( r'^%s(?P<path>.*)' % settings.MEDIA_URL.lstrip('/'),
          'django.views.static.serve',
          { 'document_root' : settings.MEDIA_ROOT, 'show_indexes': True }
        ),
    )
