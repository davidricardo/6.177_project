import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from chargen.models import *

class dWeaponResource(resources.ModelResource):
    class Meta:
        model = dWeapon

class dWeaponAdmin(ImportExportModelAdmin):
    resource_class = dWeaponResource
admin.site.register(dWeapon,dWeaponAdmin)

class dChar_classResource(resources.ModelResource):
    class Meta:
        model = dChar_class

class dChar_classAdmin(ImportExportModelAdmin):
    resource_class = dChar_classResource
    
admin.site.register(dChar_class,dChar_classAdmin)


class darmorsResource(resources.ModelResource):
    class Meta:
        model = darmors

class darmorsAdmin(ImportExportModelAdmin):
    resource_class = darmorsResource
    
admin.site.register(darmors,darmorsAdmin)

class dbackstoryResource(resources.ModelResource):
    class Meta:
        model = dbackstory

class dbackstoryAdmin(ImportExportModelAdmin):
    resource_class = dbackstoryResource
    
admin.site.register(dbackstory,dbackstoryAdmin)
class dsubclassResource(resources.ModelResource):
    class Meta:
        model = dsubclass

class dsubclassAdmin(ImportExportModelAdmin):
    resource_class = dsubclassResource
admin.site.register(dsubclass,dsubclassAdmin)

admin.site.register(user_entry)

class dspellResource(resources.ModelResource):
    class Meta:
        model = dspell

class dspellAdmin(ImportExportModelAdmin):
    resource_class = dspellResource

admin.site.register(dspell,dspellAdmin)


class dRaceResource(resources.ModelResource):
    class Meta:
        model = dRace

class dRaceAdmin(ImportExportModelAdmin):
    resource_class = dRaceResource
    

admin.site.register(dRace,dRaceAdmin)