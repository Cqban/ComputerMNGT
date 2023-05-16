from django.contrib import admin
from .models import Machine, Personnel, Infrastructure

admin.site.register(Machine)
admin.site.register(Personnel)
admin.site.register(Infrastructure)

# Register your models here.
