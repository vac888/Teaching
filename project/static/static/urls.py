"""
URL configuration for static project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sites.views import index2, index, index3, index4, index5, api_key_give, ProtectedDataView, index6
from sites.views import GenerateAPIKey

urlpatterns = [
    path('admin/', admin.site.urls),
    path('x/', index, name="index"),
    path('x/page_1.html', index2, name="index2"),
    path('generate-api-key/', GenerateAPIKey.as_view(), name='generate-api-key'),
    path('x/api_key.html', index3, name="index3"),
    path('x/index4', index4, name='index4'),
    path('x/index5', index5, name='index5'),
    path('x/api_key_give', api_key_give, name='api_key_give()'),
    path('protected-data/', ProtectedDataView.as_view(), name='protected-data'),
    path('x/info.html', index6, name='index6'),
]

