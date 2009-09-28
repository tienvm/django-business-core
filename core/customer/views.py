# Create your views here.
import datetime

from django.template import RequestContext, Context, loader
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.db import transaction
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.core.mail import send_mass_mail, send_mail
from django.utils.importlib import import_module

from dblogger.models import LogEntry
from customer.forms import AddCustomerForm
from customer.models import Customer
from django.conf import settings

def get_profile_form():
    if getattr(settings, 'CUSTOMER_PROFILE_FORM', False):
        module_string = settings.CUSTOMER_PROFILE_FORM.split('.')
        form_name = module_string[-1]
        module_name = '.'.join(module_string[0:-1])
        
        profile_module = import_module(module_name)
        FormClass = getattr(profile_module, form_name)
        return FormClass
    else:
        return None
    
#@login_required
def list(request):
    return render_to_response(
        'customer/list.html',
        locals(),
        context_instance=RequestContext(request),
    )

#@login_required
@transaction.commit_on_success
def create(request):
    FormClass = get_profile_form()
    
    if request.method == 'POST':
        if FormClass is not None:
            profile_form = FormClass(request.POST)
        else:
            profile_form = None
            
        customer_form = AddCustomerForm(request.POST)
        if customer_form.is_valid():
            customer = Customer.objects.add_customer(customer_form.cleaned_data)
        else:
            return render_to_response(
                'customer/create.html',
                locals(),
                context_instance=RequestContext(request)
            )
        if profile_form is not None and profile_form.is_valid():
            profile = profile_form.save()
            profile.customer = customer
            profile.save()
        else:
            return render_to_response(
                'customer/create.html',
                locals(),
                context_instance=RequestContext(request)
            )
        request.session['flash'] = 'Successfully added customer: %s' % customer.name
        return HttpResponseRedirect(reverse('customer.views.list'))
    else:
        if FormClass is not None:
            profile_form = FormClass()
        
        customer_form = AddCustomerForm()
        return render_to_response(
            'customer/create.html',
            locals(),
            context_instance=RequestContext(request),
        )
    
@login_required
@transaction.commit_on_success
def edit(request, obj_id, obj_type):
    if request.method == 'POST':
        pass
    else:
        pass

@login_required
def view_customer(request, customer_id):
    pass

