from django.contrib import admin
from listings.models import Player

class PlayersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'position', 'year_old')

admin.site.register(Player, PlayersAdmin)
# Register your models here.
