from django.contrib import admin
from .models import Image, Category, Teg, image_tegs, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

class quadricAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

class categoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)

class tegAdmin(admin.ModelAdmin):
    list_display = ('name_teg',)

class image_tegAdmin(admin.ModelAdmin):
    list_display = ('image_id', 'teg_id')

admin.site.register(Image, quadricAdmin)
admin.site.register(Category, categoryAdmin)
admin.site.register(Teg, tegAdmin)
admin.site.register(image_tegs, image_tegAdmin)