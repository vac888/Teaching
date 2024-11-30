from django.contrib import admin
from .models import myquadric

class quadricAdmin(admin.ModelAdmin):
    list_display = ('a', 'b', 'c', 'x1', 'x2', 'x_answer_1', 'x_answer_2', 'status_answer')

admin.site.register(myquadric, quadricAdmin)
