from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Your Name'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Question about work'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write your message body here'}), required=True)
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'placeholder':'your.own@email.com'}))