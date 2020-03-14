from django.contrib import admin
from webapp.models import Files

class FilesAdmin(admin.ModelAdmin):
    model = Files
    list_display = ('file', 'author')

admin.site.register(Files, FilesAdmin)
# Register your models here.
