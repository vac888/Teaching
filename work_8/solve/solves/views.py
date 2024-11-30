from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuadraticForm
import math


def solve_quadratic(request):
    if request.method == 'POST':
        form = QuadraticForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            answer1 = form.cleaned_data['answer1']
            answer2 = form.cleaned_data['answer2']

            if a == 0:
                result='Коэффициент a равен 0'
                check_answer = 'Решение не правильное'
            else:
                
                discriminant = b**2 - 4*a*c

                if discriminant > 0:
                    x1 = (-b + math.sqrt(discriminant)) / (2*a)
                    x2 = (-b - math.sqrt(discriminant)) / (2*a)
                    result = f"Корни уравнения: x1 = {x1}, x2 = {x2}"
                    if float(answer1) == x1 and float(answer2) == x2:
                        check_answer = 'Решение правильное'
                    else:
                        check_answer = 'Решение не правильное'
                    enter_data(a, b, c, x1, x2, answer1, answer2, check_answer)
                elif discriminant == 0:
                    x = -b / (2*a)
                    result = f"Уравнение имеет один корень: x = {x}"
                    if float(answer1) == x and float(answer2) == x:
                        check_answer = 'Решение правильное'
                    else:
                        check_answer = 'Решение не правильное'
                    enter_data(a, b, c, x, x, answer1, answer2, check_answer)
                else:
                    result = "Уравнение не имеет действительных корней"
                    if answer1 == '-' and answer2 == '-':
                        check_answer = 'Решение правильное'
                    else:
                        check_answer = 'Решение не правильное'
                        print(answer1)
                    enter_data(a, b, c, 'Нет корней!', 'Нет корней!', answer1, answer2, check_answer)
            return render(request, 'result.html', {'result': result, 'check_answer': check_answer})
    else:
        form = QuadraticForm()

    return render(request, 'solve.html', {'form': form})

def enter_data(a, b, c, x1, x2, x_answer_1, x_answer_2, status_answer):
    from solves.models import myquadric

    new_record = myquadric(a = a, b = b, c = c, x1 = x1, x2 = x2, x_answer_1 = x_answer_1, x_answer_2 = x_answer_2, status_answer = status_answer)
    new_record.save()
