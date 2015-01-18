"""
This is where code for the admin version of the site will go.
We can use the admin verson to make data entry easier.
"""

from django.contrib import admin
from chargen.models import dWeapon
admin.site.register(dWeapon)
from chargen.models import dRace
admin.site.register(dRace)
from chargen.models import dChar_class
admin.site.register(dChar_class)
from chargen.models import darmors
admin.site.register(darmors)
from chargen.models import dbackround
admin.site.register(dbackround)
from chargen.models import dsub_Char_class
admin.site.register(dsub_Char_class)
# Register your models here.
