from django.contrib import admin
from . models import Document

# Register your models here.

class AdminDocumnet(admin.ModelAdmin):
    pass


admin.site.register(Document)
