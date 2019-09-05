from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    phone_number = forms.IntegerField()