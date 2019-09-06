from django.contrib import admin
from .models import *

# Register your models here.

class WrestlerAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Name", {"fields": ["name"]}),
        ("Birthplace", {"fields": ["birthplace"]}),
        ("Image", {"fields": ["image"]}),
        ("Description", {"fields": ["description"]}),
        ("Alignment", {"fields": ["alignment"]}),
        ("Social", {"fields": ["twitter_handle", "instagram_handle"]}),
        ("Titles", {"fields": ["titles"]})
    ]


admin.site.register(Title)
admin.site.register(Wrestler, WrestlerAdmin)