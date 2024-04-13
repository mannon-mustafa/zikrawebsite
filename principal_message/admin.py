from django.contrib import admin
from principal_message.models import principal_message

#

class principal_messageAdmin(admin.ModelAdmin):
    list_display=('caption','video',)

admin.site.register(principal_message, principal_messageAdmin)
