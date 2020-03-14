from django.contrib import admin
from webapp.models import Files, Private


class FilesAdmin(admin.ModelAdmin):
    model = Files
    list_display = ('file', 'author')


class PrivateAdmin(admin.ModelAdmin):
    model = Private
    list_display = ('file', 'user')


admin.site.register(Files, FilesAdmin)
admin.site.register(Private, PrivateAdmin)
# Register your models here.
