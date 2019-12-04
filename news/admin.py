from django.contrib import admin
from .models import Articles
from .models import Host

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'content']


class HostAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'port', 'name', 'hostDesc']


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Host, HostAdmin)

