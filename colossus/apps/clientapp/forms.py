from django import forms

class SendMessageForm(forms.Form):
    title= forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recepients = forms.CharField(widget=forms.Textarea)
