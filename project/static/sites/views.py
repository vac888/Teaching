from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import APIKey
from django.contrib.auth.models import User
global amount
amount = 0
import re

def info_score_object():
    count = 0
    temp = 0

    url = 'https://blog.maximumtest.ru/post/srednij-ball-egeh-po-predmetam.html'

    response = requests.get(url)
    html_content = response.text

    object  = {}
    year = {}

    soup = BeautifulSoup(html_content, 'html.parser')

    table1 = soup.find('body')

    for i in table1.find_all('h3', 'wp-block-heading'):
        title = i.text
        object[title] = {}  # Создаем новый словарь для каждого заголовка
        count = 0  # Сбрасываем счетчик для каждого нового заголовка

        # Ищем таблицу для текущего заголовка
        table2 = i.find_next('figure', 'wp-block-table is-style-stripes')

        if table2:  # Проверяем, что таблица найдена
            for j in table2.find_all('td', 'has-text-align-center'):
                cleaned_text = re.sub(r'\s*\([^)]*\)', '', j.text)  # Убираем текст в скобках
                cleaned_text = re.sub(r'[^\d,]', '', cleaned_text)  # Убираем все, кроме цифр и запятых

                # Если текст не пустой
                if cleaned_text:
                    if count % 2 == 0:
                        temp = cleaned_text
                        count += 1
                    else:
                        # Заменяем запятую на точку в числах
                        cleaned_text = cleaned_text.replace(",", ".")
                        year[temp] = float(cleaned_text)
                        count += 1

            object[title] = year  # Сохраняем данные для текущего заголовка
            year = {}  # Очищаем словарь для следующего заголовка

    return object

@csrf_exempt
def google_search(query, num_results=5):
    # URL для поиска в Google
    url = f"https://www.google.com/search?q={query}"
    
    # Заголовки для имитации запроса от браузера
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # Выполняем GET-запрос
    response = requests.get(url, headers=headers)
    
    # Проверяем успешность запроса
    if response.status_code != 200:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return []
    
    # Парсим HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Находим результаты поиска (заголовки и ссылки)
    results = []
    for g in soup.find_all("h3"):
        # Получаем текст заголовка
        title = g.get_text()
        # Получаем ссылку (родительский элемент заголовка)
        link = g.parent.get("href")
        if title and link:
            results.append({"title": title, "link": link})
        
        # Останавливаемся, если достигли нужного количества результатов
        if len(results) >= num_results:
            break
    
    return results

from duckduckgo_search import DDGS
import time
from functools import lru_cache
@csrf_exempt
@lru_cache(maxsize=128)  # Кэшируем результаты с максимальным размером кэша 128
def get_search_results(query, max_results=5):
    time.sleep(5)
    results = DDGS().text(query, max_results=max_results)
    return results

@csrf_exempt
def index(request):
    status=-1
    return render(request, 'main.html', {'status': status})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate


@csrf_exempt
def index4(request):
    if request.method == 'POST':
        input_username3 = request.POST.get('login2')
        input_password3 = request.POST.get('password2')
        # login_check = User.objects.all()
        # for login in login_check:
        #     if login.username == input_username3:
        #         if login.password == input_password3:
        #             status = 1
        #         else:
        #             status = -1
        # else:
        #     status = -1
        
        if input_username3 and input_password3:
            user = authenticate(request, username=input_username3, password=input_password3)
            if user is not None:
                status = 1
            else:
                status = -1
        else:
            status = -1

    #return render(request, 'main.html', {'status': status})
    response = redirect('/x')
    response.set_cookie("status", status)
    if status == 1:
        response.set_cookie("login", input_username3)
        response.set_cookie("password", input_password3)
    return response

@csrf_exempt
def index5(request):
    if request.method == 'POST':
        input_username = request.POST.get('login')
        input_email = request.POST.get('email')
        input_password = request.POST.get('password')
        input_password2 = request.POST.get('password_repeat')
        if input_password == input_password2:
            exists = User.objects.filter(username=input_username).exists()
            if exists:
                print("Значение существует в таблице.")
            else:
                print("Значение не существует в таблице.")
                user = User.objects.create_user(username=input_username, password=input_password, is_superuser=0, email=input_email, is_staff = 0, is_active = 1)
    return render(request, 'main.html', {'status': status})

@csrf_exempt
def index2(request):
    # global amount
    # my_cookie_value = request.COOKIES.get('chooseObject')
    # print(my_cookie_value)

    # if my_cookie_value == 'math':
    #     query = "Средние баллы по ЕГЭ по профильной математики"
    # elif my_cookie_value == 'russian':
    #     query = "Средние баллы по ЕГЭ по русскому языку"

    # search_results = google_search(query, num_results=5)

    # object = info_score_object()
    # print(object)

    # if amount == 0:
    #     query2 = "средний балл ЕГЭ по математике"
    #     results = get_search_results(query2)
    #     print(results)
    #     amount += 1
    #     object = info_score_object()
    #     return render(request, 'page_1.html', {'object': object, 'result': results})
    # else:
    #     cached_results = get_search_results(query)
    #     print(cached_results)
    #     object = info_score_object()
    #     return render(request, 'page_1.html', {'object': object, 'result': cached_results})

    object = info_score_object()
    return render(request, 'page_1.html', {'object': object})

@csrf_exempt
def index3(request):
    return render(request, 'api_key.html')

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import APIKey

from django.contrib.auth.models import User

class GenerateAPIKey(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        print(user)
        if not user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        api_key, created = APIKey.objects.get_or_create(user=user)
        return Response({"api_key": api_key.key}, status=status.HTTP_200_OK)

@csrf_exempt
class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return None

        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            return (api_key_obj.user, None)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')

from django.http import JsonResponse

@csrf_exempt
def api_key_give(request):
    import requests

    my_cookie_value = request.COOKIES.get('login')
    my_cookie_value2 = request.COOKIES.get('password')

    url = "http://127.0.0.1:8000/generate-api-key/"
    auth = (my_cookie_value, my_cookie_value2)
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, auth=auth)

    print("Status Code:", response.status_code)
    print("Response Body:", response.json())
    #return JsonResponse(response.json(), status=response.status_code)
    return render(request, 'api_key.html', {'apicode': response.json()})

from .models import APIKey, APIKeyUsage

class ProtectedDataView(APIView):
    def get(self, request, *args, **kwargs):
        # Получаем API-ключ из заголовка
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return Response({"error": "API key is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Проверяем, существует ли API-ключ
            api_key_obj = APIKey.objects.get(key=api_key)
        except APIKey.DoesNotExist:
            return Response({"error": "Invalid API key"}, status=status.HTTP_401_UNAUTHORIZED)
        
        APIKeyUsage.objects.create(
            api_key=api_key_obj,
            request_ip=request.META.get('REMOTE_ADDR'),  # IP-адрес запроса
            request_method=request.method  # Метод запроса (GET, POST и т.д.)
        )

        # Если ключ действителен, возвращаем JSON с информацией
        usage_count = APIKeyUsage.objects.filter(api_key=api_key_obj).count()

        user = api_key_obj.user
        object=info_score_object()
        print(object)
        data = [{
            "message": "Access granted",
            'usage_count': usage_count,
            "user": {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }
        ]

        data2 = [{
            "object": {
                "object": key,
                "score": object[key].values()
            },
        }
        for key in object
        ]
        data.append(data2)
        return Response(data, status=status.HTTP_200_OK)
    
@csrf_exempt
def index6(request):
    return render(request, 'info.html')
