from django.contrib import admin
from server.models import *

# Register your models here.
admin.site.register(Categorie)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(Order)