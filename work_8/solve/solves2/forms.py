from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')