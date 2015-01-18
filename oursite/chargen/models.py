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
<<<<<<< HEAD
    
    
    
=======

>>>>>>> origin/Rachael-shmer-shmer
    def __unicode__(self):
        return self.weapon_name

    class Meta:
        app_label= 'chargen'
class Char_Race(models.Model):
    name= models.CharField(max_length=40)
    dex_mod= models.IntegerField(default=0)
    char_mod= models.IntegerField(default=0)
    str_mod= models.IntegerField(default=0)
    int_mod= models.IntegerField(default=0)
    wis_mod= models.IntegerField(default=0)
    con_mod= models.IntegerField(default=0)
    speed= models.IntegerField()
    skill_proficiencies= models.CharField(max_length=400)
    optional_skill_proficiencies= models.IntegerField(default=0)
    language= models.CharField(max_length=400)
    optional_lang_proficiencies= models.IntegerField(default=0)
    weapon_proficiencies= models.CharField(max_length=400)
    armour_proficiencies= models.CharField(max_length=100)
    tool_proficiencies= models.CharField(max_length=400)
    features=models.CharField(max_length=2000)
<<<<<<< HEAD
  
=======
>>>>>>> origin/Rachael-shmer-shmer

    def __unicode__(self):
        return self.name

    class Meta:
        app_label= 'chargen'
class job(models.Model):
    name= models.CharField(max_length=40)
    hit_die=models.IntegerField()
    armour_proficiencies= models.CharField(max_length=100)
    weapon_proficiencies= models.CharField(max_length=400)
    tool_proficiencies= models.CharField(max_length=400)
    saving_throws_proficiencies=models.CharField(max_length=400)
    skill_proficiencies= models.CharField(max_length=400)
    number_skill_proficiencies= models.IntegerField()
    features=models.CharField(max_length=3000)
    cantrips_known= models.IntegerField()
    spells_known= models.IntegerField()
    spell_slots_1st_level= models.IntegerField()
    spell_casting_ability= models.CharField(max_length=15)
    sugested_cantrips= models.CharField(max_length=2000)
    sugested_1st_level_spells= models.CharField(max_length=2000)
<<<<<<< HEAD
    

=======
>>>>>>> origin/Rachael-shmer-shmer
    def __unicode__(self):
        return self.name

    class Meta:
        app_label= 'chargen'
class armors(models.Model):
     name= models.CharField(max_length=40)
     armour_class= models.CharField(max_length=40)
     ac_mod= models.IntegerField()
     strgenth_requirement= models.IntegerField(default=0)
     disadvantage_stealth= models.BooleanField(default=False)
     very_expensive= models.BooleanField(default=False)
     moderatly_expensive= models.BooleanField(default=False)

     def __unicode__(self):
        return self.name
     class Meta:
        app_label= 'chargen'
class backround(models.Model):
    name= models.CharField(max_length=40)
    skill_proficiencies= models.CharField(max_length=400)
    language= models.CharField(max_length=400)
    tool_proficiencies= models.CharField(max_length=400)
    equipment = models.CharField(max_length=2000)
    feature = models.CharField(max_length=2000)
    



    def __unicode__(self):
        return self.name
    class Meta:
        app_label= 'chargen'
        '''

class sub_job(models.Model):
    name = models.CharField(max_length=40)
    






    def __unicode__(self):
        return self.name


    class Meta:
        app_label= 'chargen'
        '''











    
    









    
    
