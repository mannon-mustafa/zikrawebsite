from django.contrib import admin
from programs.models import programs

# Register your models here.

class programAdmin(admin.ModelAdmin):
    list_display=('caption','video',)

admin.site.register(programs, programAdmin)