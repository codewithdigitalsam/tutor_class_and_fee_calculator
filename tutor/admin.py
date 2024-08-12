
from .models import Tutor
from django.contrib import admin

@admin.register(Tutor)

class TutorAdmin(admin.ModelAdmin):
    list_display = ('mode','classhour','classdate')
