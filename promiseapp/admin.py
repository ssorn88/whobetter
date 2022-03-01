from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Candidate, Depart, DepartCon

admin.site.register(Candidate)
admin.site.register(Depart)
admin.site.register(DepartCon)


