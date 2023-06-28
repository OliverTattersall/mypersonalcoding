from django import forms

types = [
        ('beer', 'Beer'),
        ('hard liquor', 'Hard liquor'),
        ('wine', 'Wine'),
        ('coolers', 'Coolers'),
        ('ipas', 'IPAs'),
        ('ciders', 'Ciders'),
         ]
search_types = [
        ('all', 'All Drinks'),
        ('beer', 'Beer'),
        ('hardliquor', 'Hard liquor'),
        ('wine', 'Wine'),
        ('coolers', 'Coolers'),
        ('ipas', 'IPAs'),
        ('ciders', 'Ciders'),
         ]

stores = [
        ('LCBO', 'LCBO'),
        ('Beer Store', 'Beer Store'),
        ]

search_stores = [
        ('', 'All Stores'),
        ('LCBO', 'LCBO'),
        ('Beer Store', 'Beer Store'),
        ]

units = [
        (0,"All units"),
        (1,1),
        (2,2),
        (4,4),
        (6,6),
        (8,8),
        (12,12),
        (15,15),
        (18,18),
        (24,24),
        (30,30),
        (45,45),
        (48,48),
        (60,60),
]

class TestForm(forms.Form):
    link = forms.CharField(min_length=7, widget= forms.TextInput
                           (attrs={'class':'text-input'})) 
    type = forms.CharField(widget=forms.Select(choices=types))
    store = forms.CharField(widget=forms.Select(choices=stores))


class SearchForm(forms.Form):
    type = forms.CharField(widget=forms.Select(choices=search_types))
    store = forms.CharField(widget=forms.Select(choices=search_stores), required=False)
    units = forms.IntegerField(widget=forms.Select(choices=units))
    min_apd = forms.DecimalField(decimal_places=4, max_digits=7, initial=0, label='Minimum Alcohol per dollar')

