import datetime
from django.contrib.localflavor.us.forms import USStateField, USStateSelect
from django import forms

class AddCustomerForm(forms.Form):
    name = forms.CharField()
    
    #### CONTACT INFO ###
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.CharField()
    #address = forms.CharField()
    #city = forms.CharField()
    #state = USStateField(widget=USStateSelect())
    #postal_code = forms.CharField()
    
    ### USER INFO ###
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    