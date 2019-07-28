from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from happx.models import Doctor
from happx.models import patmodels





# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ('problem','DoctorType','sex')



class DocAdmin(admin.ModelAdmin):
    list_display = ('Email','Qualification','Gender','specilization')


admin.site.register(Doctor,DocAdmin)
admin.site.register(patmodels, SiteAdmin)



