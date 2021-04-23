from django import forms

class detail_form(forms.Form):
    name = forms.CharField (max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter name...'}))
    contact = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'Phone number...'}))
    url = forms.URLField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Enter URL...'}))