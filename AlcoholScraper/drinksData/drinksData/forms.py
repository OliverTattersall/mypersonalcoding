from django import forms

types = [
        ('beer', 'Beer'),
        ('hardliquor', 'Hard liquor'),
        ('wine', 'Wine'),
        ('coolers', 'Coolers'),
        ('ipas', 'IPAs'),
         ]

stores = [
        ('LCBO', 'LCBO'),
        ('Beer Store', 'Beer Store'),
        ]

class TestForm(forms.Form):
    link = forms.CharField(min_length=7, widget= forms.TextInput
                           (attrs={'class':'text-input'})) 
    type = forms.CharField(widget=forms.Select(choices=types))
    store = forms.CharField(widget=forms.Select(choices=stores))
