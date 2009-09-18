from django import forms

class CustomerProfile(forms.Form):
    plan = forms.CharField()
    