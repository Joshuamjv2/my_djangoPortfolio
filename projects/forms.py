from django import forms
from django.forms import widgets

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name*'}))
    email = forms.CharField(max_length=200, required=True, widget = forms.TextInput(attrs={'placeholder': 'Email Address*'}))
    message = forms.CharField(required=True, widget = forms.Textarea(attrs={'placeholder': 'Your Message*', 'rows':6, 'cols':30}))