from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image, Category, image_tegs, Teg

def index(request):
    from sites.models import Image
    images = Image.objects.using('mydatabase2').all()
    return render(request, 'page_1.html', {'images': images})

def index2(request):
    from sites.models import Image
    images = Image.objects.using('mydatabase2').all()
    return render(request, 'page_2.html', {'images': images})

def index3(request):
    from sites.models import Image
    images = Image.objects.using('mydatabase2').all()
    return render(request, 'page_info.html', {'images': images})

def index4(request):
    from sites.models import Image
    category = Category.objects.using('mydatabase2').all()
    images = Image.objects.using('mydatabase2').all()
    return render(request, 'category.html', {'category': category, 'images': images})

def index5(request):
    from sites.models import Image
    image_and_tegs = image_tegs.objects.using('mydatabase2').all()
    images = Image.objects.using('mydatabase2').all()
    tegs = Teg.objects.using('mydatabase2').all()
    return render(request, 'tegs.html', {'image_teg': image_and_tegs, 'images': images, 'tegs': tegs})