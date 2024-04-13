from django.contrib import admin
from marquee.models import  marquee, notice_board, image_slider

# Register your models here.

class marqueeAdmin(admin.ModelAdmin):
    list_display=('news_item',)

admin.site.register(marquee, marqueeAdmin)


class notice_boardAdmin(admin.ModelAdmin):
    list_display=('heading','notice')

admin.site.register(notice_board, notice_boardAdmin)

class image_sliderAdmin(admin.ModelAdmin):
    list_display=('image',)
admin.site.register(image_slider, image_sliderAdmin)