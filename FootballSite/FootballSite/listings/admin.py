from django.contrib import admin
from listings.models import Players

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'position', 'year_old')

admin.site.register(Players, PlayersAdmin)
# Register your models here.
