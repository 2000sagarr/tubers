from django.contrib import admin
from django.utils.html import format_html

from .models import Youtuber

# Register your models here.

class YTAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40"')
    list_display = ('id','myphoto' ,'name','subs_count','is_featured')
    search_fields = ('name',)
    list_filter = ('city',  'camera_type')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured','subs_count', )

admin.site.register(Youtuber, YTAdmin)