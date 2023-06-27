from django import forms

class TestForm(forms.Form):
    link = forms.CharField(min_length=7) 
    type = forms.CharField(min_length=4)
