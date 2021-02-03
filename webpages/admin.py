from django.contrib import admin
from django.utils.html import format_html
#import models
from .models import Slider, Team

#for model admin inline
# to display info on admin panel
class TeamAdmin(admin.ModelAdmin):
    # this function is used to add photo into admin panel
    def myphoto(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40"')

    # value to show
    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    # clickable value
    list_display_links = ('first_name', )
    # search field
    search_fields = ('first_name', 'role')
    #filter option
    list_filter = ('role',)

# Register your models here.
#slider model
admin.site.register(Slider)
#team model
admin.site.register(Team, TeamAdmin)
