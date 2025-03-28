# forms.py

from django import forms

class ExampleForm(forms.Form):
    # Add some fields as an example
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
