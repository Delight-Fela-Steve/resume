from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label='Your Full Name', max_length=50)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)