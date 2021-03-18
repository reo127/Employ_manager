from django.contrib import admin
from main_manager.models import Employe
from main_manager.models import ChildEmploye

# Register your models here.

admin.site.register(Employe)
admin.site.register(ChildEmploye)
