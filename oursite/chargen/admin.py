"""
This is where code for the admin version of the site will go.
We can use the admin verson to make data entry easier.
"""

from django.contrib import admin
from chargen.models import Weapon
admin.site.register(Weapon)
from chargen.models import Char_Race
admin.site.register(Char_Race)
from chargen.models import job
admin.site.register(job)

# Register your models here.
