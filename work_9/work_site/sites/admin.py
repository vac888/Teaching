from django.contrib import admin
from .models import Image

class quadricAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(Image, quadricAdmin)
