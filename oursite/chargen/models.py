"""
This is where models, which are tables, will be created.

See https://docs.djangoproject.com/en/1.6/intro/tutorial01/ , 
https://docs.djangoproject.com/en/1.6/ref/models/instances/#django.db.models.Model , or
https://docs.djangoproject.com/en/1.6/howto/custom-model-fields/ for more information.
"""

from django.db import models

# Create your models here.

class Weapon(models.Model):
    weapon_name= models.CharField(max_length=30)
    martial_arts= models.BooleanField(default=False)
    mele= models.BooleanField(default=True)
    finesse= models.BooleanField(default=False)
    damage_type= models.CharField(max_length=20)
    two_handed= models.BooleanField(default=False)
    number_of_damage_die= models.IntegerField()
    type_of_damage_die= models.IntegerField()
    range_close= models.IntegerField(default=0, blank=True)
    range_max=models.IntegerField(default=0,blank=True)
    
    
    
    
    def __unicode__(self):
        return self.weapon_name
class Race(models.Model):
    name= models.CharField(max_length=25)
    dex_mod= models.IntegerField(default=0)
    char_mod= models.IntegerField(default=0)
    str_mod= models.IntegerField(default=0)
    int_mod= models.IntegerField(default=0)
    wis_mod= models.IntegerField(default=0)
    con_mod= models.IntegerField(default=0)
    speed= models.IntegerField()
    
