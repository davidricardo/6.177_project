"""


from django.conf import settings

settings.configure(TEMPLATE_DIRS=('/oursite/templates',), DEBUG=False,
                   TEMPLATE_DEBUG=False)

from chargen.models import Weapon


print Weapon.objects.all()
"""
"""
from oursite import settings
DJANGO_SETTINGS_MODULE = settings
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from chargen.models import Weapon
from django.core import serializers


print serializers.serialize( "python", Weapon.objects.all() )
