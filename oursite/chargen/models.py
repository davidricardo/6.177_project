"""
This is where models, which are tables, will be created.

See https://docs.djangoproject.com/en/1.6/intro/tutorial01/ , 
https://docs.djangoproject.com/en/1.6/ref/models/instances/#django.db.models.Model , or
https://docs.djangoproject.com/en/1.6/howto/custom-model-fields/ for more information.
"""

from django.db import models

# Create your models here.

class dWeapon(models.Model):
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

    class Meta:
        app_label= 'chargen'
class dRace(models.Model):
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
  

    def __unicode__(self):
        return self.name
        
    class Meta:
        app_label= 'chargen'
class dChar_class(models.Model):
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
    

    def __unicode__(self):
        return self.name

    class Meta:
        app_label= 'chargen'
class darmors(models.Model):
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
class dbackstory(models.Model):
    name= models.CharField(max_length=40)
    skill_proficiencies= models.CharField(max_length=400)
    language= models.CharField(max_length=400)
    optional_lang_proficiencies= models.IntegerField(default=0)
    tool_proficiencies= models.CharField(max_length=400)
    equipment = models.CharField(max_length=2000)
    feature = models.CharField(max_length=2000)
    



    def __unicode__(self):
        return self.name
    class Meta:
        app_label= 'chargen'
        

class dsub_class(models.Model):
    name = models.CharField(max_length=40)
    level_1_feature = models.CharField(max_length=2000)
    level_2_feature = models.CharField(max_length=2000)
    level_3_feature = models.CharField(max_length=2000)
    level_4_feature = models.CharField(max_length=2000)
    level_5_feature = models.CharField(max_length=2000)
    level_6_feature = models.CharField(max_length=2000)
    level_7_feature = models.CharField(max_length=2000)
    level_8_feature = models.CharField(max_length=2000)
    level_9_feature = models.CharField(max_length=2000)
    level_10_feature = models.CharField(max_length=2000)
    level_11_feature = models.CharField(max_length=2000)
    level_12_feature = models.CharField(max_length=2000)
    level_13_feature = models.CharField(max_length=2000)
    level_14_feature = models.CharField(max_length=2000)
    level_15_feature = models.CharField(max_length=2000)
    level_16_feature = models.CharField(max_length=2000)
    level_17_feature = models.CharField(max_length=2000)
    level_18_feature = models.CharField(max_length=2000)
    level_19_feature = models.CharField(max_length=2000)
    level_20_feature = models.CharField(max_length=2000)
    

    def __unicode__(self):
        return self.name


    class Meta:
        app_label= 'chargen'
        

class user_entry(models.Model):
    name = models.CharField(max_length=40)
    char_class= models.ForeignKey('dChar_class')
    sub_class= models.ForeignKey('dsub_class')
    race= models.ForeignKey('dRace')
    strgenth=models.IntegerField()
    dexterity=models.IntegerField()
    constitution=models.IntegerField()
    intelegence=models.IntegerField()
    wisdom=models.IntegerField()
    charisma=models.IntegerField()
    level=models.IntegerField(default=1)
    backround= models.ForeignKey('dbackstory')
    


    def __unicode__(self):
        return self.name


    class Meta:
        app_label= 'chargen'
        

class spell(models.Model):
    char_class= models.ForeignKey('dChar_class')
    sub_class= models.ForeignKey('dsub_class')
    level=models.IntegerField()
    known_cantrips= models.IntegerField()
    known_spell_level1= models.IntegerField()
    known_spell_level2= models.IntegerField()
    known_spell_level3= models.IntegerField()
    known_spell_level4= models.IntegerField()
    known_spell_level5= models.IntegerField()
    known_spell_level6= models.IntegerField()
    known_spell_level7= models.IntegerField()
    known_spell_level18= models.IntegerField()
    known_spell_level9=models.IntegerField()
    slots_or_prepered_spell_level1= models.IntegerField()
    slots_or_prepered_spell_level2= models.IntegerField()
    slots_or_prepered_spell_level3= models.IntegerField()
    slots_or_prepered_spell_level4= models.IntegerField()
    slots_or_prepered_spell_level5= models.IntegerField()
    slots_or_prepered_spell_level6= models.IntegerField()
    slots_or_prepered_spell_level7= models.IntegerField()
    slots_or_prepered_spell_level8= models.IntegerField()
    slots_or_prepered_spell_level9=models.IntegerField()
    possible_spells_level1= models.IntegerField()
    possible_spells_level2= models.IntegerField()
    possible_spells_level3= models.IntegerField()
    possible_spells_level4= models.IntegerField()
    possible_spells_level5= models.IntegerField()
    possible_spells_level6= models.IntegerField()
    possible_spells_level7= models.IntegerField()
    possible_spells_level8= models.IntegerField()
    possible_spells_level9= models.IntegerField()
    total_spells= models.IntegerField()
    minium_1st_level_spells= models.IntegerField()


    def __unicode__(self):
        return self.sub_class


    class Meta:
        app_label= 'chargen'
        






    
    









    
    
