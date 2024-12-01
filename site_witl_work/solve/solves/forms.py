from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label='Коэффициент a')
    b = forms.FloatField(label='Коэффициент b')
    c = forms.FloatField(label='Коэффициент c')
    answer1 = forms.CharField(label='Введите свое первое решение')
    answer2 = forms.CharField(label='Введите свое второе решение')