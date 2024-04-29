from django import forms

from . models import Contact
# create your forms below

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email', 'class':'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject','class':'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Message', 'class':'form-control', 'rows':'4'}))