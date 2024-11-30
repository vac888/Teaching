from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def index(request):
    from sites.models import Image
    images = Image.objects.all()
    return render(request, 'page_1.html', {'images': images})

def index2(request):
    from sites.models import Image
    images = Image.objects.all()
    return render(request, 'page_2.html', {'images': images})

def index3(request):
    from sites.models import Image
    images = Image.objects.all()
    return render(request, 'page_info.html', {'images': images})