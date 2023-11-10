from django.contrib import admin
from notice.models import notice,Head_Master_Message, Gallery, Sliders, smc, club
# Register your models here.
class noticeAdmin(admin.ModelAdmin):
    list_display=('id','notice_title','notice_description','notice_date')
admin.site.register(notice,noticeAdmin)

#Gallary
class galleryAdmin(admin.ModelAdmin):
    list_display=('title','image')
admin.site.register(Gallery,galleryAdmin)

#Slider
class slidersAdmin(admin.ModelAdmin):
    list_display=('title','short_description','image')
admin.site.register(Sliders,slidersAdmin)

#add head master info in index page
class headmasterAdmin(admin.ModelAdmin):
    list_display=('message','image')
admin.site.register(Head_Master_Message,headmasterAdmin)

#smc
class smcAdmin(admin.ModelAdmin):
    list_display=('title','image','date')
admin.site.register(smc,smcAdmin)

#club
class clubAdmin(admin.ModelAdmin):
    list_display=('title','image','page')
admin.site.register(club,clubAdmin)
