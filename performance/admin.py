from django.contrib import admin
from performance.models import  performance


# Register your models here.

class performanceAdmin(admin.ModelAdmin):
    list_display=('name','rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri','conduct','fee_status',)

admin.site.register(performance, performanceAdmin)



