from django.contrib import admin
from .models import Material, Article, Nummernkreise, MouldingMachine, Customer, Tooling, Stock

admin.site.register(Material)
admin.site.register(Article)
admin.site.register(Stock)
admin.site.register(MouldingMachine)
admin.site.register(Customer)
admin.site.register(Tooling)
admin.site.register(Nummernkreise)