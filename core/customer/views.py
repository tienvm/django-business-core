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

from dblogger.models import LogEntry

@login_required
def list(request):
    pass

@login_required
@transaction.commit_on_success
def create(request):
    if request.method == 'POST':
        pass
    else:
        pass
    
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

