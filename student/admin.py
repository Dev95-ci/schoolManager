from django.contrib import admin
from .models import Eleve

class StudentAdmin(admin.ModelAdmin):
    search_fields = ()

admin.site.register(Eleve)
