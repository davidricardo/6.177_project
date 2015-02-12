import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from chargen.models import *
"""
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

class dRaceResource(resources.ModelResource):
    class Meta:
        model = dRace

class dRaceAdmin(ImportExportModelAdmin):
    resource_class = dRaceResource
    

admin.site.register(dRace,dRaceAdmin)

class dpersonalitiesResource(resources.ModelResource):
    class Meta:
        model = dpersonalities

class dpersonalitiesAdmin(ImportExportModelAdmin):
    resource_class = dpersonalitiesResource
    

admin.site.register(dpersonalities,dpersonalitiesAdmin)

class dbondsResource(resources.ModelResource):
    class Meta:
        model = dbonds

class dbondsAdmin(ImportExportModelAdmin):
    resource_class = dbondsResource
    

admin.site.register(dbonds,dbondsAdmin)

class didealsResource(resources.ModelResource):
    class Meta:
        model = dideals

class didealsAdmin(ImportExportModelAdmin):
    resource_class = didealsResource
    

admin.site.register(dideals,didealsAdmin)

class dflawsResource(resources.ModelResource):
    class Meta:
        model = dflaws

class dflawsAdmin(ImportExportModelAdmin):
    resource_class = dflawsResource
    

admin.site.register(dflaws,dflawsAdmin)

class dDescriptionResource(resources.ModelResource):
    class Meta:
        model = dDescription

class dDescriptionAdmin(ImportExportModelAdmin):
    resource_class = dDescriptionResource


admin.site.register(dDescription,dDescriptionAdmin)


class dabilityweightsResource(resources.ModelResource):
    class Meta:
        model = dabilityweights

class dabilityweightsAdmin(ImportExportModelAdmin):
    resource_class = dabilityweightsResource


admin.site.register(dabilityweights,dabilityweightsAdmin)

"""
