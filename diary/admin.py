from django.contrib import admin
from diary.models import  *



# Register your models here.

class diaryAdmin_fees(admin.ModelAdmin):
    list_display=('rollno','grade','fee_status',)
admin.site.register(diary_fees, diaryAdmin_fees)

class diaryAdmin_nur(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_nursary, diaryAdmin_nur)


class diaryAdmin_lkg(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_lkg, diaryAdmin_lkg)


class diaryAdmin_ukg(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_ukg, diaryAdmin_ukg)


class diaryAdmin_first(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_first, diaryAdmin_first)


class diaryAdmin_second(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_second, diaryAdmin_second)


class diaryAdmin_third(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_third, diaryAdmin_third)


class diaryAdmin_fourth(admin.ModelAdmin):
    list_display=('rollno','grade','english','urdu','sst','math','science','computer','islamiyat','kashmiri',)

admin.site.register(diary_fourth, diaryAdmin_fourth)

# Register your models here.
