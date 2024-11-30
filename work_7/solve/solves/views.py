from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuadraticForm
import math


def solve_quadratic(request):
    
    a = float(request.GET[('a')])
    b = float(request.GET[('b')])
    c = float(request.GET[('c')])

    if a == 0:
        result='Коэффициент a равен 0'
    else:       
        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            result = f"Корни уравнения: x1 = {x1}, x2 = {x2}"
        elif discriminant == 0:
            x = -b / (2*a)
            result = f"Уравнение имеет один корень: x = {x}"
        else:
            result = "Уравнение не имеет действительных корней"

    return render(request, 'result.html', {'result': result})
