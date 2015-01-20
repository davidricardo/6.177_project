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
        

class dsubclass(models.Model):
    name = models.CharField(max_length=40)
    char_class=models.ForeignKey('dChar_class')
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
    sub_class= models.ForeignKey('dsubclass')
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
        

class dspell(models.Model):
    char_class= models.ForeignKey('dChar_class')
    sub_class= models.ForeignKey('dsubclass')
    level=models.IntegerField()
    slots_or_prepered_spell_level1= models.IntegerField(default=0)
    slots_or_prepered_spell_level2= models.IntegerField(default=0)
    slots_or_prepered_spell_level3= models.IntegerField(default=0)
    slots_or_prepered_spell_level4= models.IntegerField(default=0)
    slots_or_prepered_spell_level5= models.IntegerField(default=0)
    slots_or_prepered_spell_level6= models.IntegerField(default=0)
    slots_or_prepered_spell_level7= models.IntegerField(default=0)
    slots_or_prepered_spell_level8= models.IntegerField(default=0)
    slots_or_prepered_spell_level9=models.IntegerField(default=0)
    possible_spells_level1= models.IntegerField(default=0)
    possible_spells_level2= models.IntegerField(default=0)
    possible_spells_level3= models.IntegerField(default=0)
    possible_spells_level4= models.IntegerField(default=0)
    possible_spells_level5= models.IntegerField(default=0)
    possible_spells_level6= models.IntegerField(default=0)
    possible_spells_level7= models.IntegerField(default=0)
    possible_spells_level8= models.IntegerField(default=0)
    possible_spells_level9= models.IntegerField(default=0)
    cantrips_known= models.IntegerField()
    total_spells= models.IntegerField()
    minium_1st_level_spells= models.IntegerField()


    def __unicode__(self):
        name=self.char_class.name +" "+ self.sub_class.name + " level "+ str(self.level)
        return name


    class Meta:
        app_label= 'chargen'
    

spells= {'aid':2,
         'alarm':2,
         'alter self':2,
         'animal friendship':1,
         'animal messanger':2,
         'animal shapes':8,
         'animate dead':3,
         'animate object':5,
         'antilife shell':5,
         'antimagic field':8,
         'antipath/sympath':8,
         'arcane eye':4,
         'arcane gate':6,
         'arcane lock':2,
         'armor of agathys':1,
         'arms of haydar':1,
         'astral projection':9,
         'augury':2,
         'aura of life':4,
         'aura of purity':4,
         'aura of vitality':3,
         'awaken':5,
         'bane':1,
         'banishing smite':5,
         'banishment':4,
         'barkskin':2,
         'beacon of hope':3,
         'beast sense':2,
         'bestow curse'3,
         'bigbys hanb':5,
         'blade barrier':6,
         'bless':1,
         'blight':4,
         'blinding smite':3,
         'blindness/deafness':2,
         'blink':3,
         'blur':2,
         'branding smite':2,
         'burning hands':1,
         'call lightning':3,
         'calm amotions':2,
         'chain lightning':6,
         'charm person':1,
         'chromatic orb':1,
         'circle of death':6,
         'circle of power':5,
         'clairvoyance':3,
         'clone':8,
         'cloud of daggers':2,
         'cloudkill':5,
         'color spray':1,
         'comand':1,
         'commune':5,
         'commune with nature':5,
         'compelled duel':1,
         'comprehend languages':1,
         'compulsion':4,
         'cone of cold':5,
         'cone of confusion':4,
         'conjure animals':3,
         'conjure barrage':3,
         'conjure celestial':7,
         'conjure elemental':5,
         'conjure fey':6,
         'conjure minor elementals':4,
         'conjure volley':5,
         'conjure woodlnad beings':4,
         'contact other plane':5,
         'contagion':5,
         'contingency':6,
         'continual flame':2,
         'control water':4,
         'control weather':8,
         'cordon of arrows':2,
         'counterspell':3,
         'create food and water':3,
         'dreate or destroy water':1,
         'create undead':6,
         'creation':5,
         'crown of madness':2,
         'crusaders mantle':3,
         'cure woundds':1,
         'darkness':2,
         'darkvision':2,
         'daylight':3,
         'death ward':4,
         'delayed blast fireball':7,
         'demiplane':8,
         'destructive wave':5,
         'detect evil and good':1,
         'detect magic':1,
         'detect poison and disease':1,
         'detect thoughts':2,
         'dimension door':4,
         'disguise self':1,
         'disentegrate':6,
         'dispel evil and good':5,
         'dispel magic':3,
         'dissonant whispers':1,
         'divination':4,
         'divine favor':1,
         'divine word':7,
         'dominate beast':4,
         'dominate monster':8,
         'dominate person':5,
         'drawmijs instant summons':6,
         'dream':5,
         'earthquake':8,
         'elemantal weapon':3,
         'enhanse ability':2,
         'enalrge/reduce':2,
         'ensnaring strike':1,
         'entangle':1,
         'enthrall';2,
         'etheralness':7,
         'evards black tentacles':4,
         'expiditious retreat':1,
         'eyebite':6,
         'fabricate':4,
         'farie fire':1,
         'false life':1,
         'fear':3,
         'feather fall':1,
         'feeblemind':8,
         'feign death':3,
         'find familiar':1,
         'find steed':2,
         'find path':6,
         'find traps':2,
         'finger of death':7,
         'fireball':3,
         'fire shield':4,
         'fire dtorm':7,
         'fire blade':2,
         'flame strike':5,
         'flaming sphere':2,
         'flesh to stone':6,
         'fly':3,
         'fog cloud':1,
         'forbiddance':6,
         'forcecage':7,
         'foresight':9,
         'freedom of movement':4,
         'gaseous form':3,
         'gate':9,
         'geas':5,
         'gentle repose':2,
         'giant insect':4,
         'glibness':8,         
         'globe of invulnerability':6,
         'glyph of warding':3,
         'goodberry':1,
         'grasping vine':4,
         'grease':1,
         'greater invisibility':4,
         'greater restoation':5,
         'guuardian of faith':4,
         'guards and wards':6,
         'guiding bolt':1,
         'gust of wind':2,
         'hail of thorns':1,
         'hallow':5,
         'hallucinatory terrain':4,
         'harm':6,
         'haste':3,
         'heal':6,
         'healing word':1,
         'heat metal':2,
         'hellish rebuke':1,
         'heroes feast':6,
         'heroism':1,
         'hex':1,
         'hold monster':5,
         'hold person':2,
         'holy aura':8,
         'hunger of hadar':3,
         'hunters mask':1,
         'hyponotic pattern':3,
         'ice storm':4,
         'identify':1,
         'illousory script':1,
         'imprisonment':9,
         'incendiary cloud':8,
         'inflict wounds':1,
         'insect plague':5,
         'invisibility':2,
         'jump':1,
         'knock':2,
         'legend lore':5,
         'leomunds secret chest':4,
         'leomunds tiny hut':3,
         'lesser restoration':2,
         'lightning arrow':3,
         'lightning bolt':3,
         'locate animals or plants':2,
         'locate creature':4,
         'locate object':2,
         'longstrider':1,
         'mage armor':1,
         'magic circle':3,
         'magic jar':6,
         'magic missile':1,
         'magic mouth':2,
         'magic weapon':2,
         'major image':3,
         'mass cure wounds':5,
         'mass heal':9,
         'mass healing word':3,
         'masss sugestion':6,
         'meld into stone':3,
         'melfs acid arrow':2,
         'meteor swarm':9,
         'mind blank':8,
         'mirage arcane':7,
         'mirror image':2,
         'mislead':5,
         'misty step':2,
         'modify memory':5,
         'moonbeam':2,
         'mordenkainens faithful hounds':4,
         'mordenkainens magnificent mannsion':7,
         'mordenkainens private ssenctum':4,
         'mordenkainens sword':7,
         'move earth':6,
         'nondetection':3,
         '
         
         
         
         

         
    
    









    
    
