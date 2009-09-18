import datetime

from django import forms

class AddCustomerForm(forms.Form):
    name = forms.CharField()
    