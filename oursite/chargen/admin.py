"""
This is where code for the admin version of the site will go.
We can use the admin verson to make data entry easier.
"""
import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from chargen.models import dWeapon

class dWeaponResource(resources.ModelResource):
    class Meta:
        model = dWeapon

class dWeaponAdmin(ImportExportModelAdmin):
    resource_class = dWeaponResource
admin.site.register(dWeapon)

from chargen.models import dRace
from chargen.models import dChar_class

class dChar_classResource(resources.ModelResource):
    class Meta:
        model = dChar_class

class dChar_classAdmin(ImportExportModelAdmin):
    resource_class = dChar_classResource
    
admin.site.register(dChar_class)

from chargen.models import darmors

class darmorsResource(resources.ModelResource):
    class Meta:
        model = darmors

class darmorsAdmin(ImportExportModelAdmin):
    resource_class = darmorsResource
    
admin.site.register(darmors)

from chargen.models import dbackstory

class dbackstoryResource(resources.ModelResource):
    class Meta:
        model = dbackstory

class dbackstoryAdmin(ImportExportModelAdmin):
    resource_class = dbackstoryResource
    
admin.site.register(dbackstory)
from chargen.models import dsubclass

class dsubclassResource(resources.ModelResource):
    class Meta:
        model = dsubclass

class dsubclassAdmin(ImportExportModelAdmin):
    resource_class = dsubclassResource
admin.site.register(dsubclass)
from chargen.models import user_entry
admin.site.register(user_entry)
from chargen.models import dspell

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
    

admin.site.register(dRace)
