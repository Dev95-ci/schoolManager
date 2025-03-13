from django.contrib import admin
from .models import Classe

class ClasseAdmin(admin.ModelAdmin):
    list_display = ("nom", "niveau", "annee_scolaire")

admin.site.register(Classe, ClasseAdmin)
