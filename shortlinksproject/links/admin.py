from django.contrib import admin
from .models import Links
# Register your models here.

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'shortlink', 'link', 'user')
    list_display_links = ('id', 'title')
    search_fields = ('title','shortlink')


admin.site.register(Links, LinksAdmin)