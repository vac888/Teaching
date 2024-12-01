"""
URL configuration for solve project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, register_converter
from solves.views import solve_quadratic
from solves2.views import solve_quadratic2
from sites.views import index, index2, index3, index4, index5
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('x/', solve_quadratic),
    path('x2/', solve_quadratic2),
    path('x3/', index),
    path('x3/page_2.html', index2),
    path('x3/page_1.html', index),
    path('x3/page_info.html', index3),
    path('x3/category.html', index4),
    path('x3/tegs.html', index5)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)