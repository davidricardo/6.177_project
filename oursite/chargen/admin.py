"""
This is where code for the admin version of the site will go.
We can use the admin verson to make data entry easier.
"""
import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from django.contrib import admin
from chargen.models import dWeapon


<<<<<<< HEAD
class dWeaponAdmin(ImportExportModelAdmin):
    resource_class = dWeaponResource
admin.site.register(dWeapon,dWeaponAdmin)
=======
admin.site.register(dWeapon)
>>>>>>> FETCH_HEAD

from chargen.models import dRace
from chargen.models import dChar_class

    
admin.site.register(dChar_class,dChar_classAdmin)

from chargen.models import darmors

    
admin.site.register(darmors,darmorsAdmin)

from chargen.models import dbackstory

    
admin.site.register(dbackstory,dbackstoryAdmin)
from chargen.models import dsubclass

<<<<<<< HEAD
class dsubclassResource(resources.ModelResource):
    class Meta:
        model = dsubclass

class dsubclassAdmin(ImportExportModelAdmin):
    resource_class = dsubclassResource
admin.site.register(dsubclass,dsubclassAdmin)
=======
admin.site.register(dsubclass)
>>>>>>> FETCH_HEAD
from chargen.models import user_entry
admin.site.register(user_entry)
from chargen.models import dspell


admin.site.register(dspell)


    

admin.site.register(dRace,dRaceAdmin)
