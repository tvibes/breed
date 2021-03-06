from django.contrib import admin
from .models import Artisan


class ArtisanAdmin(admin.ModelAdmin):
    display = [
        ('Description', {'fields': ['title', 'image', 'description', 'detail']}),
    ]

    class Meta:
        model = Artisan


admin.site.register(Artisan, ArtisanAdmin)






