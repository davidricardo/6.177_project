#stores Character objects
#accessed by views.py and pdftest.py
import math, random

import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from models import *
from collections import OrderedDict
from NameGen import RandomNameGenerator
from SpellLists import *

#the skill in each key is ruled by the ability that is the value of that key:
#means that that skill check is equal to the modifier of the ruling ability
RULING_ABILITIES = {
    "acrobatics": "dexterity",
    "animal handling":"wisdom",
    "arcana": "intelligence",
    "athletics": "strength",
    "deception": "charisma",
    "history": "intelligence",
    "insight": "wisdom",
    "intimidation": "charisma",
    "investigation": "intelligence",
    "medicine": "wisdom",
    "nature": "intelligence",
    "perception": "wisdom",
    "performance": "charisma",
    "persuasion": "charisma",
    "religion": "intelligence",
    "sleight of hand": "dexterity",
    "stealth": "dexterity",
    "survival": "wisdom"
}

RACES = [
    "Dwarf - Hill",
    "Dwarf - Mountain",
    "Elf - High",
    "Elf - Wood",
    "Elf - Dark (Drow)",
    "Halfling - Lightfoot",
    "Halfling - Stout",
    "Human",
    "Dragonborn",
    "Gnome - Forest",
    "Gnome - Rock",
    "Half-Elf",
    "Half-Orc",
    "Tiefling"
    ]

#list of all six ability scores
ABILITY_SCORES = [
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma"
    ]

#instruments given in handbook
INSTRUMENTS = ["bagpipes",
               "drum",
               "dulcimer",
               "flute",
               "lute",
               "lyre",
               "horn",
               "pan flute",
               "shawm",
               "viol"
               ]

#list of all skills, used when choosing proficiencies from whole skill list
SKILLS_TOTAL = [
    "acrobatics",
    "animal handling",
    "arcana",
    "athletics",
    "deception",
    "history",
    "insight",
    "intimidation",
    "investigation",
    "medicine",
    "nature",
    "perception",
    "performance",
    "persuasion",
    "religion",
    "sleight of hand",
    "stealth",
    "survival"
]

#abbreviations used in database
ABILITY_KEYS = {"strength":"str",
                "dexterity":"dex",
                "constitution":"con",
                "intelligence":"int",
                "wisdom":"wis",
                "charisma":"char"}

#languages given in handbook
LANGUAGES = [
    "Abyssal",
    "Celestial",
    "Common",
    "Deep Speech",
    "Draconic",
    "Druidic",
    "Dwarvish",
    "Elvish",
    "Giant",
    "Gnomish",
    "Goblin",
    "Halfling",
    "Infernal",
    "Orc",
    "Primordial",
    "Sylvan",
    "Thieves Cant",
    "Undercommon"
]

#main class which holds all information for character
class Character:
    def __init__(self, name, char_class,subclass, race, background, strength = 10,dexterity = 10, constitution = 10, intelligence = 10, wisdom = 10, charisma = 10, level=1):
        self.languages = []
        self.equipment = []
        self.proficiencies = {"weapon":[],"armor":[],"skill":[],"saves":[],"tools":[]}
        self.features = []
        self.weapons = []
        self.expertise = [] #skills you get double proficiency to; only a few classes/races get these
        self.cantrips = []
        self.spells1 = []
        self.spells2 = []
        self.spells3 = []
        self.spells4 = []
        self.spells5 = []
        self.spells6 = []
        self.spells7 = []
        self.spells8 = []
        self.spells9 = []
        self.spelllist1 = []
        self.spelllist2 = []
        self.spelllist3 = []
        self.spelllist4 = []
        self.spelllist5 = []
        self.spelllist6 = []
        self.spelllist7 = []
        self.spelllist8 = []
        self.spelllist9 = []
        self.armor = ""
        self.level = level #this tool defaults to 1 but in future higher levels may be supported
        self.name = name
        if char_class=="":
            number_of_records = dChar_class.objects.count()
            random_index = random.randrange(0,number_of_records)
            char_class = dChar_class.objects.all()[random_index].name
        if strength==8 and dexterity==8 and constitution==8 and intelligence==8 and wisdom==8 and charisma==8:
            self.ability_scores = self.generateAbilityScores(char_class)
        else:
            self.ability_scores = ability_scores={"strength":strength,"dexterity":dexterity,"constitution":constitution,"intelligence":intelligence,"wisdom":wisdom,"charisma":charisma}
        self.background = Background(self,background)
        self.my_race = Race(self, race)
        self.my_class = Char_Class(self, char_class,subclass)
        if name=="":
            self.name = self.generateName()
        self.skills = {"acrobatics":0,"animal handling":0,"arcana":0,"athletics":0,"deception":0,"history":0,"insight":0,"intimidation":0,"investigation":0,"medicine":0,"nature":0,"perception":0,"performance":0,"persuasion":0,"religion":0,"sleight of hand":0,"stealth":0,"survival":0}
        self.saves = {"strength":0,"dexterity":0,"constitution":0,"intelligence":0,"wisdom":0,"charisma":0}
        self.features = [x.lower() for x in self.features]
        while "feat" in self.features:
            self.features.remove("feat")
        self.equipment = [x.lower() for x in self.equipment]
        self.equipment = list(set(self.equipment))
        self.languages = [x.lower() for x in self.languages]
        self.languages = list(set(self.languages))
        self.weapons = [x.lower() for x in self.weapons]
        self.weapons = list(set(self.weapons))

        #unique feature of Rogues, hard-coded
        if self.my_class.class_name=="Rogue":
            x = random.randrange(0,len(self.proficiencies["skill"]))
            y = random.randrange(0,len(self.proficiencies["skill"]))
            while y==x:
                y = random.randrange(0,len(self.proficiencies["skill"]))
            self.expertise.extend([self.proficiencies["skill"][x],self.proficiencies["skill"][y]])

        for key in self.proficiencies.keys():
            self.proficiencies[key] = list(set(self.proficiencies[key]))

        #sets all skill and save modifiers
        for s in self.skills.keys():
            self.skills[s] = self.calculate_skill(s)
        for v in self.saves.keys():
            self.saves[v] = self.calculate_save(v)

        self.equipment.extend(self.weapons)
        if "unarmed strike" in self.equipment:
            self.equipment.remove("unarmed strike")
        if self.armor !="":
            self.equipment.append(self.armor + " armor")
        if "javelin" in self.equipment:
            self.equipment.remove("javelin")
        if "dart" in self.equipment:
            self.equipment.remove("dart")
        if "handaxe" in self.equipment and "2 handaxes" in self.equipment:
            self.equipment.remove("handaxe")
        if "shortsword" in self.equipment and "2 shortswords" in self.equipment:
            self.equipment.remove("shortsword")

        #pdf file takes 12 first level spells and 8 cantrips, this prevents errors    
        while len(self.spells1)<12:
            self.spells1.append("")
        while len(self.spells2)<13:
            self.spells2.append("")
        while len(self.spells3)<13:
            self.spells3.append("")
        while len(self.spells4)<13:
            self.spells4.append("")
        while len(self.spells5)<9:
            self.spells5.append("")
        while len(self.spells6)<9:
            self.spells6.append("")
        while len(self.spells7)<9:
            self.spells7.append("")
        while len(self.spells8)<7:
            self.spells8.append("")
        while len(self.spells9)<7:
            self.spells9.append("")
        while len(self.cantrips)<8:
            self.cantrips.append("")

        #sets main three weapons to be displayed, calculates their attack and damage bonuses
        self.wpn1 = ""
        self.wpn1a = ""
        self.wpn1d = ""
        self.wpn2 = ""
        self.wpn2a = ""
        self.wpn2d = ""
        self.wpn3 = ""
        self.wpn3a = ""
        self.wpn3d = ""
        if len(self.weapons)>0:
            self.wpn1 = self.weapons[0]
            if dWeapon.objects.get(weapon_name=self.wpn1).mele==True and not(dWeapon.objects.get(weapon_name=self.wpn1).finesse==True and self.get_modifier(self.ability_scores["strength"])<self.get_modifier(self.ability_scores["dexterity"])):
                self.wpn1a = pre(self.get_proficiency_bonus()+self.get_modifier(self.ability_scores["strength"]))
                if self.get_modifier(self.ability_scores["strength"])==0:
                    bonus = ""
                else:
                    bonus = pre(self.get_modifier(self.ability_scores["strength"])) +" "
                self.wpn1d = str(dWeapon.objects.get(weapon_name=self.wpn1).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=self.wpn1).type_of_damage_die) + " " + bonus +dWeapon.objects.get(weapon_name=self.wpn1).damage_type[0] + "."
            else:
                self.wpn1a = pre(self.get_proficiency_bonus()+self.get_modifier(self.ability_scores["dexterity"]))
                if self.get_modifier(self.ability_scores["dexterity"])==0:
                    bonus = ""
                else:
                    bonus = pre(self.get_modifier(self.ability_scores["dexterity"])) +" "
                self.wpn1d = str(dWeapon.objects.get(weapon_name=self.wpn1).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=self.wpn1).type_of_damage_die) + " " + bonus +dWeapon.objects.get(weapon_name=self.wpn1).damage_type[0] + "."
            if len(self.weapons)>1:
                self.wpn2 = self.weapons[1]
                if dWeapon.objects.get(weapon_name=self.wpn2).mele==True and not(dWeapon.objects.get(weapon_name=self.wpn2).finesse==True and self.get_modifier(self.ability_scores["strength"])<self.get_modifier(self.ability_scores["dexterity"])):
                    self.wpn2a = pre(self.get_proficiency_bonus()+self.get_modifier(self.ability_scores["strength"]))
                    if self.get_modifier(self.ability_scores["strength"])==0:
                        bonus = ""
                    else:
                        bonus = pre(self.get_modifier(self.ability_scores["strength"])) +" "
                    self.wpn2d = str(dWeapon.objects.get(weapon_name=self.wpn2).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=self.wpn2).type_of_damage_die)  +" "+ bonus +dWeapon.objects.get(weapon_name=self.wpn2).damage_type[0] + "."
                else:
                    self.wpn2a = pre(self.get_proficiency_bonus()+self.get_modifier(self.ability_scores["dexterity"]))
                    if self.get_modifier(self.ability_scores["dexterity"])==0:
                        bonus = ""
                    else:
                        bonus = pre(self.get_modifier(self.ability_scores["dexterity"])) +" "
                    self.wpn2d = str(dWeapon.objects.get(weapon_name=self.wpn2).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=self.wpn2).type_of_damage_die) + " " + bonus +dWeapon.objects.get(weapon_name=self.wpn2).damage_type[0] + "."
            if len(self.weapons)>2:
                self.wpn3 = self.weapons[2]
                if dWeapon.objects.get(weapon_name=self.wpn3).mele==True and not(dWeapon.objects.get(weapon_name=self.wpn3).finesse==True and self.get_modifier(self.ability_scores["strength"])<self.get_modifier(self.ability_scores["dexterity"])):
                    self.wpn3a = pre(self.get_proficiency_bonus()+self.get_modifier(self.ability_scores["strength"]))
                    if self.get_modifier(self.ability_scores["strength"])==0:
                        bonus = ""
                    else:
                        bonus = pre(self.get_modifier(self.ability_scores["strength"])) +" "
                    self.wpn3d = str(dWeapon.objects.get(weapon_name=self.wpn3).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=self.wpn3).type_of_damage_die) + " " + bonus +dWeapon.objects.get(weapon_name=self.wpn3).damage_type[0] + "."
                else:
                    self.wpn3a = pre(self.get_proficiency_bonus()+self.get_modifier(self.ability_scores["dexterity"]))
                    if self.get_modifier(self.ability_scores["dexterity"])==0:
                        bonus = ""
                    else:
                        bonus = pre(self.get_modifier(self.ability_scores["dexterity"])) +" "
                    self.wpn3d = str(dWeapon.objects.get(weapon_name=self.wpn3).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=self.wpn3).type_of_damage_die) + " " + bonus +dWeapon.objects.get(weapon_name=self.wpn3).damage_type[0] + "."

    #calculates passive perception (10+perception modifier)
    def get_passive_perception(self):
        return 10+self.skills["perception"]
    
    #returns proficiency bonus, calculated from level
    def get_proficiency_bonus(self):
        return int(1+math.ceil(self.level/4.0))
    
    #returns modifier on ability score
    def get_modifier(self, score):
        return int(math.floor((score-10)/2.0))

    def generateAbilityScores(self,char_class):
        if random.randrange(0,4)==0:
            l = [16,14,12,10,10,8]
        elif random.randrange(0,3)==0:
            l = [15,14,14,10,10,8]
        elif random.randrange(0,2)==0:
            l = [15,14,12,12,10,9]
        else:
            l = [16,13,12,11,10,9]
        points = {"8":0,"9":1,"10":2,"11":3,"12":4,"13":5,"14":7,"15":9,"16":12,"17":15,"18":19}
        scores = {}
        wts = {}
        wts["strength"] = dabilityweights.objects.get(name=char_class).strength
        wts["dexterity"] = dabilityweights.objects.get(name=char_class).dexterity
        wts["constitution"] = dabilityweights.objects.get(name=char_class).constitution
        wts["intelligence"] = dabilityweights.objects.get(name=char_class).intelligence
        wts["wisdom"] = dabilityweights.objects.get(name=char_class).wisdom
        wts["charisma"] = dabilityweights.objects.get(name=char_class).charisma
        for x in range(1,4):
            for key in wts.keys():
                if wts[key]==x:
                    scores[key] = l.pop(0)
                    wts[key] = 0
                    for key in wts.keys():
                        if wts[key]==x:
                            wts[key] = 6
                    break
        for key in wts.keys():
            if wts[key]==6:
                scores[key] = l.pop(0)
                wts[key] = 0
        return scores

    #returns initiative modifier (just the dex modifier)
    def get_initiative(self):
        return self.get_modifier(self.ability_scores["dexterity"])
    
    #calculates skills from ruling abilities and proficiencies
    #accounts for some class and race specific skill bonuses
    def calculate_skill(self,skill):
        if (self.my_race.name[0:4]=="Dwar" or self.my_race.name=="Gnome - Rock") and skill=="history":
            return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])+2*self.get_proficiency_bonus()
        if skill in self.proficiencies["skill"]:
            if self.my_class.class_name=="Rogue" or self.my_class.class_name=="Cleric":
                if skill in self.expertise:
                    return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])+2*self.get_proficiency_bonus()
            return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])+self.get_proficiency_bonus()
        else:
            if self.my_class.subclass=="Champion" and self.level>=7 and (RULING_ABILITIES[skill]=="strength" or RULING_ABILITIES[skill]=="constitution" or RULING_ABILITIES[skill]=="dexterity"):
                return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]]) + int(math.ceil(self.get_proficiency_bonus()/2.0))
            return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])

    #calculates saves from abilities and proficiencies
    def calculate_save(self,save):
        if save in self.proficiencies["saves"]:
            return self.get_modifier(self.ability_scores[save])+self.get_proficiency_bonus()
        elif ABILITY_KEYS[save] in self.proficiencies["saves"]:
            return self.get_modifier(self.ability_scores[save])+self.get_proficiency_bonus()
        else:
            return self.get_modifier(self.ability_scores[save])

    #calculates max hit points (health) based on class and level      
    def get_max_hit_points(self):
        bonus = 0
        if self.my_race.name=="Dwarf - Hill":
            bonus += self.level
        if self.my_class.subclass=="Draconic Bloodline":
            bonus += self.level
        if self.level==1:
            return self.my_class.hit_die+self.get_modifier(self.ability_scores["constitution"])+bonus
        else:
            return self.level*(self.my_class.hit_die/2+1+self.get_modifier(self.ability_scores["constitution"]))+bonus

    #calculates armor class (defense) based on armor and dex
    def get_armor_class(self):
        dex = self.get_modifier(self.ability_scores["dexterity"])
        if self.armor=="":
            if self.my_class.class_name=="Barbarian":
                return 10 + dex + self.get_modifier(self.ability_scores["constitution"])
            if self.my_class.class_name=="Monk":
                return 10 + dex + self.get_modifier(self.ability_scores["wisdom"])
            if self.my_class.subclass=="Draconic Bloodline":
                return 13+dex
            return 10 + dex
        armor = darmors.objects.get(name=self.armor)
        if armor.armour_class=="light":
            return armor.ac_mod + dex
        if armor.armour_class=="medium":
            if dex>=2:
                return armor.ac_mod+2
            else:
                return armor.ac_mod+dex
        return armor.ac_mod

    def generateName(self):
        return RandomNameGenerator.randomname(self.my_race.name)
        
def highestScore(character):
    highest = ""
    high = 0
    for key in character.ability_scores.keys():
        if character.ability_scores[key]>high and character.ability_scores[key]+1<=20:
            highest = key
            high = character.ability_scores[key]
    return highest

def highestOdd(character):
    highest = ""
    high = 0
    for key in character.ability_scores.keys():
        if character.ability_scores[key]>high and character.ability_scores[key]+1<=20 and character.ability_scores[key]%2==1:
            highest = key
            high = character.ability_scores[key]
    return highest

def abilityScoreIncrease(character):
    if character.ability_scores[highestScore(character)]%2==1:
        character.ability_scores[highestScore(character)]+=1
        if highestOdd(character)=="":
            character.ability_scores[highestScore(character)]+=1
        else:
            character.ability_scores[highestOdd(character)]+=1
    else:
        character.ability_scores[highestScore(character)]+=2
        
#class containing the character's class
#class in d&d is like your job (Rogue, Bard, Wizard, Fighter, etc.)
#we name it Char_Class to distinguish from python classes
#classes give you equipment, features, languages, proficiencies, spells, etc.
class Char_Class:
    def __init__(self, character, name, subclass):
        self.class_name = name
        self.languages = []
        dclass = dChar_class.objects.get(name=name)
        self.subclass = subclass #subclasses are specific paths within classes, given slightly different features and stats
        if not(self.class_name=="Fighter" or self.class_name=="Rogue"):
            if character.level>=4:
                abilityScoreIncrease(character)
            if character.level>=8:
                abilityScoreIncrease(character)
            if character.level>=12:
                abilityScoreIncrease(character)
            if character.level>=16:
                abilityScoreIncrease(character)
            if character.level>=19:
                abilityScoreIncrease(character)
        if self.class_name=="Fighter":
            if character.level>=4:
                abilityScoreIncrease(character)
            if character.level>=6:
                abilityScoreIncrease(character)
            if character.level>=8:
                abilityScoreIncrease(character)
            if character.level>=12:
                abilityScoreIncrease(character)
            if character.level>=14:
                abilityScoreIncrease(character)
            if character.level>=16:
                abilityScoreIncrease(character)
            if character.level>=19:
                abilityScoreIncrease(character)
        if self.class_name=="Rogue":
            if character.level>=4:
                abilityScoreIncrease(character)
            if character.level>=6:
                abilityScoreIncrease(character)
            if character.level>=8:
                abilityScoreIncrease(character)
            if character.level>=10:
                abilityScoreIncrease(character)
            if character.level>=12:
                abilityScoreIncrease(character)
            if character.level>=16:
                abilityScoreIncrease(character)
            if character.level>=19:
                abilityScoreIncrease(character)
        if self.class_name=="Barbarian" and character.level==20:
            character.ability_scores["strength"]+=4
            character.ability_scores["constitution"]+=4
        if self.subclass=="":
            number_of_records = dsubclass.objects.filter(char_class = dChar_class.objects.get(name=name)).count()
            random_index = random.randrange(0,number_of_records)
            self.subclass = dsubclass.objects.filter(char_class = dChar_class.objects.get(name=name))[random_index].name
        #only clerics, warlocks, and sorcerers get their subclass at first level
        if name=="Cleric":
            if self.subclass=="Life Domain":
                character.spells1.extend(["bless","cure wounds"])
                character.proficiencies["armor"].append("heavy")
                if character.level>=3:
                    character.spells2.extend(["lesser restoration","spiritual weapon"])
                if character.level>=5:
                    character.spells3.extend(["beacon of hope","revivify"])
                if character.level>=7:
                    character.spells4.extend(["death ward","guardian of faith"])
                if character.level>=9:
                    character.spells5.extend(["mass cure wounds","dead"])
            if self.subclass=="Light Domain":
                character.spells1.extend(["burning hands","faerie fire"])
                character.cantrips.append("light")
                if character.level>=3:
                    character.spells2.extend(["flaming sphere","scorching ray"])
                if character.level>=5:
                    character.spells3.extend(["daylight","fireball"])
                if character.level>=7:
                    character.spells4.extend(["guardian of faith","wall of fire"])
                if character.level>=9:
                    character.spells5.extend(["flame strike","scrying"])
            if self.subclass=="Nature Domain":
                character.spells1.extend(["animal friendship","speak with animals"])
                x = random.randrange(0,len(DRUID_CANTRIPS))
                character.cantrips.append(DRUID_CANTRIPS[x])
                character.expertise.extend(choosex(["animal handling","nature","survival"],1,character.proficiencies["skill"]))
                if character.level>=3:
                    character.spells2.extend(["barkskin","spike growth"])
                if character.level>=5:
                    character.spells3.extend(["plant growth","wind wall"])
                if character.level>=7:
                    character.spells4.extend(["dominate beast","grasping vine"])
                if character.level>=9:
                    character.spells5.extend(["insect plague","tree stride"])
            if self.subclass=="Knowledge Domain":
                character.spells1.extend(["command","identify"])
                self.languages.extend(choose(LANGUAGES,2,character.languages))
                character.expertise.extend(choosex(["arcana","history","nature","religion"],2,character.proficiencies["skill"]))
                if character.level>=3:
                    character.spells2.extend(["augury","suggestion"])
                if character.level>=5:
                    character.spells3.extend(["nondetection","speak with dead"])
                if character.level>=7:
                    character.spells4.extend(["arcane eye","confusion"])
                if character.level>=9:
                    character.spells5.extend(["legend lore","scrying"])
            if self.subclass=="Trickery Domain":
                character.spells1.extend(["charm person","disguise self"])
                if character.level>=3:
                    character.spells2.extend(["mirror person","pass without trace"])
                if character.level>=5:
                    character.spells3.extend(["blink","dispel magic"])
                if character.level>=7:
                    character.spells4.extend(["dimension door","polymorph"])
                if character.level>=9:
                    character.spells5.extend(["dominate person","modify memory"])
            if self.subclass=="Tempest Domain":
                character.spells1.extend(["fog cloud","thunderwave"])
                character.proficiencies["armor"].append("heavy")
                character.proficiencies["weapon"].append("martial")
                if character.level>=3:
                    character.spells2.extend(["gust of wind","shatter"])
                if character.level>=5:
                    character.spells3.extend(["call lightning","sleet storm"])
                if character.level>=7:
                    character.spells4.extend(["control water","ice storm"])
                if character.level>=9:
                    character.spells5.extend(["destructive wave","insect plague"])
            if self.subclass=="War Domain":
                character.spells1.extend(["divine favor","shield of faith"])
                character.proficiencies["armor"].append("heavy")
                character.proficiencies["weapon"].append("martial")
                if character.level>=3:
                    character.spells2.extend(["magic weapon","spiritual weapon"])
                if character.level>=5:
                    character.spells3.extend(["crusader's mantle","spirit guardians"])
                if character.level>=7:
                    character.spells4.extend(["freedom of movement","stoneskin"])
                if character.level>=9:
                    character.spells5.extend(["flame strike","hold monster"])
        elif name=="Sorcerer":
            if self.subclass=="Draconic Bloodline":
                self.languages.append("draconic")
        elif name=="Warlock":
            if self.subclass=="The Archfey":
                character.spelllist1.extend(["faerie fire","sleep"])
                character.spelllist2.extend(["calm emotions","phantasmal force"])
                character.spelllist3.extend(["blink","plant growth"])
                character.spelllist4.extend(["dominate beast","greater invisibility"])
                character.spelllist5.extend(["dominate person","seeming"])
            if self.subclass=="The Fiend":
                character.spelllist1.extend(["burning hands","command"])
                character.spelllist2.extend(["blindness/deafness","scorching ray"])
                character.spelllist3.extend(["fireball","stinking cloud"])
                character.spelllist4.extend(["fire shield","wall of fire"])
                character.spelllist5.extend(["flame strike","hallow"])
            if self.subclass=="The Great Old One":
                character.spelllist1.extend(["dissonant whispers","Tasha's hideous laughter"])
                character.spelllist2.extend(["detect thoughts","phantasmal force"])
                character.spelllist3.extend(["clairvoyance","sending"])
                character.spelllist4.extend(["dominate beast","Evard's black tentacles"])
                character.spelllist5.extend(["dominate person","telekinesis"])
        elif character.level>=2 and (name=="Druid" or name=="Wizard"):
            if name=="Druid":
                if self.subclass=="Circle of the Land":
                    x = random.randrange(0,len(DRUID_CANTRIPS))
                    character.cantrips.append(DRUID_CANTRIPS[x])
                    x = random.randrange(0,8)
                    if x==0:
                        if character.level>=3:
                            character.spells2.extend(["hold person","spike growth"])
                        if character.level>=5:
                            character.spells3.extend(["sleet storm","slow"])
                        if character.level>=7:
                            character.spells4.extend(["freedom of movement","ice storm"])
                        if character.level>=9:
                            character.spells5.extend(["commune with nature","cone of cold"])
                    elif x==1:
                        if character.level>=3:
                            character.spells2.extend(["mirror image","misty step"])
                        if character.level>=5:
                            character.spells3.extend(["water breathing","water walk"])
                        if character.level>=7:
                            character.spells4.extend(["control water","freedom of movement"])
                        if character.level>=9:
                            character.spells5.extend(["conjure elemental","scrying"])
                    elif x==2:
                        if character.level>=3:
                            character.spells2.extend(["blur","silence"])
                        if character.level>=5:
                            character.spells3.extend(["create food and water","protection from energy"])
                        if character.level>=7:
                            character.spells4.extend(["blight","hallucinatory terrain"])
                        if character.level>=9:
                            character.spells5.extend(["insect plague","wall of stone"]) 
                    elif x==3:
                        if character.level>=3:
                            character.spells2.extend(["barkskin","spider climb"])
                        if character.level>=5:
                            character.spells3.extend(["call lightning","plant growth"])
                        if character.level>=7:
                            character.spells4.extend(["divination","freedom of movement"])
                        if character.level>=9:
                            character.spells5.extend(["commune with nature","tree stride"]) 
                    elif x==4:
                        if character.level>=3:
                            character.spells2.extend(["invisibility","pass without trace"])
                        if character.level>=5:
                            character.spells3.extend(["daylight","haste"])
                        if character.level>=7:
                            character.spells4.extend(["divination","freedom of movement"])
                        if character.level>=9:
                            character.spells5.extend(["dream","insect plague"])    
                    elif x==5:
                        if character.level>=3:
                            character.spells2.extend(["spider climb","spike growth"])
                        if character.level>=5:
                            character.spells3.extend(["lightning bolt","meld into stone"])
                        if character.level>=7:
                            character.spells4.extend(["stone shape","stoneskin"])
                        if character.level>=9:
                            character.spells5.extend(["passwall","wall of stone"])    
                    elif x==6:
                        if character.level>=3:
                            character.spells2.extend(["darkness","melf's acid arrow"])
                        if character.level>=5:
                            character.spells3.extend(["water walk","stinking cloud"])
                        if character.level>=7:
                            character.spells4.extend(["freedom of movement","locate creature"])
                        if character.level>=9:
                            character.spells5.extend(["insect plague","scrying"])     
                    elif x==7:
                        if character.level>=3:
                            character.spells2.extend(["spider climb","web"])
                        if character.level>=5:
                            character.spells3.extend(["gaseous form","stinking cloud"])
                        if character.level>=7:
                            character.spells4.extend(["greater invisibility","stone shape"])
                        if character.level>=9:
                            character.spells5.extend(["cloudkill","insect plague"])     
            elif name=="Wizard":
                if self.subclass=="School of Illusion":
                    character.cantrips.append("minor illusion")
                elif self.subclass=="School of Necromancy" and character.level>=6:
                    character.spells5.append("animate dead")
                elif self.subclass=="School of Transmutation" and character.level>=10:
                    character.spells4.append("polymorph")
        elif character.level>=3:
            if name=="Barbarian":
                if self.subclass=="Path of the Totem Warrior":
                    character.spells1.append("speak with animals")
                    character.spells2.append("beast sense")
                    self.spell_casting_ability = ""
                    self.spell_save_dc = ""
                    self.spell_atk_bonus = ""
                    self.spell_slots1 = ""
                    self.spell_slots2 = ""
                    self.spell_slots3 = ""
                    self.spell_slots4 = ""
                    self.spell_slots5 = ""
                    self.spell_slots6 = ""
                    self.spell_slots7 = ""
                    self.spell_slots8 = ""
                    self.spell_slots9 = ""
            elif name=="Bard":
                if self.subclass=="College of Lore":
                    character.proficiencies["skill"].extend(choose(SKILLS_TOTAL,3,character.proficiencies["skill"]))
                    #SIXTH LEVEL PICK TWO SPELLS FROM ANY DANG CLASS
                else:
                    character.proficiencies["armor"].extend(["medium","shields"])
                    character.proficiencies["weapon"].append("martial")
            elif name=="Fighter":
                if self.subclass=="Eldritch Knight":
                    if character.level<10:
                        character.cantrips.extend(choose(WIZARD_CANTRIPS,2,character.cantrips))
                    else:
                        character.cantrips.extend(choose(WIZARD_CANTRIPS,3,character.cantrips))
                    self.spell_slots9 = ""
                    self.spell_slots8 = ""
                    self.spell_slots7 = ""
                    self.spell_slots6 = ""
                    self.spell_slots5 = ""
                    self.spell_slots4 = ""
                    self.spell_slots3 = ""
                    self.spell_slots2 = ""
                    self.spell_slots1 = ""
                    level = str(character.level)
                    spellsKnown = KNIGHTK[level]
                    if KNIGHT4[level]>0:
                        q = random.randrange(1,KNIGHT4[level]+2)
                        character.spells4.extend(choose(AE4,q,character.spells4))
                        spellsKnown -= q;
                        self.spell_slots4 = KNIGHT4[level]
                    if KNIGHT3[level]>0:
                        q = random.randrange(1,KNIGHT3[level]+1)
                        character.spells3.extend(choose(AE3,q,character.spells3))
                        spellsKnown -= q;
                        self.spell_slots3 = KNIGHT3[level]
                    if KNIGHT2[level]>0:
                        q = random.randrange(2,KNIGHT2[level]+1)
                        character.spells2.extend(choose(AE2,q,character.spells2))
                        spellsKnown -= q;
                        self.spell_slots2 = KNIGHT2[level]
                    self.spell_slots1 = KNIGHT1[level]
                    q = spellsKnown
                    character.spells1.extend(choose(AE1,q,character.spells1)) 
                    self.spell_casting_ability = "intelligence"
                    self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
                    self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            elif name=="Monk":
                #ELEMENTAL MAGIC CRAP
                pass
            elif name=="Paladin":
                if self.subclass=="Oath of Devotion":
                    if character.level>=3:
                        character.spells1.extend(["protection from evil and good","sanctuary"])
                    if character.level>=5:
                        character.spells2.extend(["lesser restoration","zone of truth"])
                    if character.level>=9:
                        character.spells3.extend(["beacon of hope","dispel magic"])
                    if character.level>=13:
                        character.spells4.extend(["freedom of movement","guardian of faith"])
                    if character.level>=17:
                        character.spells5.extend(["commune","flame strike"])
                if self.subclass=="Oath of the Ancients":
                    if character.level>=3:
                        character.spells1.extend(["ensnaring strike","speak with animals"])
                    if character.level>=5:
                        character.spells2.extend(["moonbeam","misty step"])
                    if character.level>=9:
                        character.spells3.extend(["plant growth","protection from energy"])
                    if character.level>=13:
                        character.spells4.extend(["ice storm","stoneskin"])
                    if character.level>=17:
                        character.spells5.extend(["commune with nature","tree stride"])
                if self.subclass=="Oath of Vengeance":
                    if character.level>=3:
                        character.spells1.extend(["bane","hunter's mark"])
                    if character.level>=5:
                        character.spells2.extend(["hold person","misty step"])
                    if character.level>=9:
                        character.spells3.extend(["haste","protection from energy"])
                    if character.level>=13:
                        character.spells4.extend(["banishment","dimension door"])
                    if character.level>=17:
                        character.spells5.extend(["hold monster","scrying"])
            elif name=="Ranger":
                pass
            elif name=="Rogue":
                if self.subclass=="Assassin":
                    character.proficiencies["tools"].extend(["disguise kit","poisoner's kit"])
                if self.subclass=="Arcane Trickster":
                    if character.level<10:
                        character.cantrips.extend(choose(WIZARD_CANTRIPS,3,character.cantrips))
                    else:
                        character.cantrips.extend(choose(WIZARD_CANTRIPS,4,character.cantrips))
                    self.spell_slots9 = ""
                    self.spell_slots8 = ""
                    self.spell_slots7 = ""
                    self.spell_slots6 = ""
                    self.spell_slots5 = ""
                    self.spell_slots4 = ""
                    self.spell_slots3 = ""
                    self.spell_slots2 = ""
                    self.spell_slots1 = ""
                    level = str(character.level)
                    spellsKnown = TRICKK[level]
                    if TRICK4[level]>0:
                        q = random.randrange(1,TRICK4[level]+2)
                        character.spells4.extend(choose(EI4,q,character.spells4))
                        spellsKnown -= q;
                        self.spell_slots4 = TRICK4[level]
                    if TRICK3[level]>0:
                        q = random.randrange(1,TRICK3[level]+1)
                        character.spells3.extend(choose(EI3,q,character.spells3))
                        spellsKnown -= q;
                        self.spell_slots3 = TRICK3[level]
                    if TRICK2[level]>0:
                        q = random.randrange(2,TRICK2[level]+1)
                        character.spells2.extend(choose(EI2,q,character.spells2))
                        spellsKnown -= q;
                        self.spell_slots2 = TRICK2[level]
                    self.spell_slots1 = TRICK1[level]
                    q = spellsKnown
                    character.spells1.extend(choose(EI1,q,character.spells1)) 
                    self.spell_casting_ability = "intelligence"
                    self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
                    self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
        self.hit_die = dclass.hit_die
        weapons = string_to_list(dclass.weapon_proficiencies.lower())
        armor = string_to_list(dclass.armour_proficiencies.lower())
        tools = string_to_list(dclass.tool_proficiencies.lower())
        saves = string_to_list(dclass.saving_throws_proficiencies.lower())
        skills = choose(string_to_list(dclass.skill_proficiencies),dclass.number_skill_proficiencies,character.proficiencies["skill"])
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":saves,"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.equipment = []
        self.get_equipment(character)
        character.equipment.extend(self.equipment)
        self.features = []
        self.get_features(character)
        character.features.extend(self.features)
        if self.class_name == "Druid":
            self.languages.append("druidic")
        if self.class_name == "Rogue":
            self.languages.append("thieves' cant")
        character.languages.extend(self.languages)
        
        #if class casts spell at first level, sets those spells
        spellcastingclasses = ["Druid","Cleric","Bard","Wizard","Sorcerer","Warlock"]
        if self.class_name in spellcastingclasses:
            self.spell_slots9 = ""
            self.spell_slots8 = ""
            self.spell_slots7 = ""
            self.spell_slots6 = ""
            self.spell_slots5 = ""
            self.spell_slots4 = ""
            self.spell_slots3 = ""
            self.spell_slots2 = ""
            self.spell_slots1 = ""
            for key in ABILITY_KEYS.keys():
                if ABILITY_KEYS[key]==dclass.spell_casting_ability.lower():
                    self.spell_casting_ability = key
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            if self.class_name=="Wizard":
                level = str(character.level)
                spellsKnown = character.level+character.get_modifier(character.ability_scores["intelligence"])
                if spellsKnown<1:
                    spellsKnown==1
                character.cantrips.extend(choose(WIZARD_CANTRIPS,WIZARDC[level],character.cantrips))
                if WIZARD9[level]>0:
                    character.spells9.extend(choose(WIZARD_SPELLS9,1,character.spells9))
                    spellsKnown -= 1;
                    self.spell_slots9 = WIZARD9[level]
                if WIZARD8[level]>0:
                    character.spells8.extend(choose(WIZARD_SPELLS8,1,character.spells8))
                    spellsKnown -= 1;
                    self.spell_slots8 = WIZARD8[level]
                if WIZARD7[level]>0:
                    q = random.randrange(1,WIZARD7[level]+1)
                    character.spells7.extend(choose(WIZARD_SPELLS7,q,character.spells7))
                    spellsKnown -= q;
                    self.spell_slots7 = WIZARD7[level]
                if WIZARD6[level]>0:
                    q = random.randrange(1,WIZARD6[level]+1)
                    character.spells6.extend(choose(WIZARD_SPELLS6,q,character.spells6))
                    spellsKnown -= q;
                    self.spell_slots6 = WIZARD6[level]
                if WIZARD5[level]>0:
                    q = random.randrange(1,WIZARD5[level]+1)
                    character.spells5.extend(choose(WIZARD_SPELLS5,q,character.spells5))
                    spellsKnown -= q;
                    self.spell_slots5 = WIZARD5[level]
                if WIZARD4[level]>0:
                    q = random.randrange(1,WIZARD4[level]+2)
                    character.spells4.extend(choose(WIZARD_SPELLS4,q,character.spells4))
                    spellsKnown -= q;
                    self.spell_slots4 = WIZARD4[level]
                if WIZARD3[level]>0:
                    q = random.randrange(1,WIZARD3[level]+1)
                    character.spells3.extend(choose(WIZARD_SPELLS3,q,character.spells3))
                    spellsKnown -= q;
                    self.spell_slots3 = WIZARD3[level]
                if WIZARD2[level]>0:
                    q = random.randrange(2,WIZARD2[level]+1)
                    character.spells2.extend(choose(WIZARD_SPELLS2,q,character.spells2))
                    spellsKnown -= q;
                    self.spell_slots2 = WIZARD2[level]
                self.spell_slots1 = WIZARD1[level]
                q = spellsKnown
                character.spells1.extend(choose(WIZARD_SPELLS1,q,character.spells1)) 
            if self.class_name=="Warlock":
                spell_list = []
                level = str(character.level)
                spellsKnown = WARLOCKK[level]
                character.cantrips.extend(choose(WARLOCK_CANTRIPS,WARLOCKC[level],character.cantrips))
                if WARLOCKL[level]==1:
                    self.spell_slots1 = WARLOCKS[level]
                    spells = choose(WARLOCK_SPELLS1,spellsKnown,character.spells1)
                    for spell in spells:
                        if spell in WARLOCK_SPELLS1:
                            character.spells1.append(spell)
                if WARLOCKL[level]==2:
                    self.spell_slots2 = WARLOCKS[level]
                    spell_list = WARLOCK_SPELLS1[:]
                    spell_list.extend(WARLOCK_SPELLS2)
                    spells  = choose(spell_list,spellsKnown,character.spells2)
                    for spell in spells:
                        if spell in WARLOCK_SPELLS1:
                            character.spells1.append(spell)
                        elif spell in WARLOCK_SPELLS2:
                            character.spells2.append(spell)
                if WARLOCKL[level]==3:
                    self.spell_slots3 = WARLOCKS[level]
                    spell_list = WARLOCK_SPELLS1[:]
                    spell_list.extend(WARLOCK_SPELLS2)
                    spell_list.extend(WARLOCK_SPELLS3)
                    spells  = choose(spell_list,spellsKnown,character.spells3)
                    for spell in spells:
                        if spell in WARLOCK_SPELLS1:
                            character.spells1.append(spell)
                        elif spell in WARLOCK_SPELLS2:
                            character.spells2.append(spell)
                        elif spell in WARLOCK_SPELLS3:
                            character.spells3.append(spell)
                if WARLOCKL[level]==4:
                    self.spell_slots4 = WARLOCKS[level]
                    spell_list = WARLOCK_SPELLS1[:]
                    spell_list.extend(WARLOCK_SPELLS2)
                    spell_list.extend(WARLOCK_SPELLS3)
                    spell_list.extend(WARLOCK_SPELLS4)
                    spells  = choose(spell_list,spellsKnown,character.spells4)
                    for spell in spells:
                        if spell in WARLOCK_SPELLS1:
                            character.spells1.append(spell)
                        elif spell in WARLOCK_SPELLS2:
                            character.spells2.append(spell)
                        elif spell in WARLOCK_SPELLS3:
                            character.spells3.append(spell)
                        elif spell in WARLOCK_SPELLS4:
                            character.spells4.append(spell)
                if WARLOCKL[level]==5:
                    self.spell_slots5 = WARLOCKS[level]
                    spell_list = WARLOCK_SPELLS1[:]
                    spell_list.extend(WARLOCK_SPELLS2)
                    spell_list.extend(WARLOCK_SPELLS3)
                    spell_list.extend(WARLOCK_SPELLS4)
                    spell_list.extend(WARLOCK_SPELLS5)
                    spells  = choose(spell_list,spellsKnown,character.spells5)
                    for spell in spells:
                        if spell in WARLOCK_SPELLS1:
                            character.spells1.append(spell)
                        elif spell in WARLOCK_SPELLS2:
                            character.spells2.append(spell)
                        elif spell in WARLOCK_SPELLS3:
                            character.spells3.append(spell)
                        elif spell in WARLOCK_SPELLS4:
                            character.spells4.append(spell)
                        elif spell in WARLOCK_SPELLS5:
                            character.spells5.append(spell)
            if self.class_name=="Sorcerer":
                level = str(character.level)
                spellsKnown = SORCERERK[level]
                character.cantrips.extend(choose(SORCERER_CANTRIPS,SORCERERC[level],character.cantrips))
                if SORCERER9[level]>0:
                    character.spells9.extend(choose(SORCERER_SPELLS9,1,character.spells9))
                    spellsKnown -= 1;
                    self.spell_slots9 = SORCERER9[level]
                if SORCERER8[level]>0:
                    character.spells8.extend(choose(SORCERER_SPELLS8,1,character.spells8))
                    spellsKnown -= 1;
                    self.spell_slots8 = SORCERER8[level]
                if SORCERER7[level]>0:
                    q = random.randrange(1,SORCERER7[level]+1)
                    character.spells7.extend(choose(SORCERER_SPELLS7,q,character.spells7))
                    spellsKnown -= q;
                    self.spell_slots7 = SORCERER7[level]
                if SORCERER6[level]>0:
                    q = random.randrange(1,SORCERER6[level]+1)
                    character.spells6.extend(choose(SORCERER_SPELLS6,q,character.spells6))
                    spellsKnown -= q;
                    self.spell_slots6 = SORCERER6[level]
                if SORCERER5[level]>0:
                    q = random.randrange(1,SORCERER5[level]+1)
                    character.spells5.extend(choose(SORCERER_SPELLS5,q,character.spells5))
                    spellsKnown -= q;
                    self.spell_slots5 = SORCERER5[level]
                if SORCERER4[level]>0:
                    q = random.randrange(1,SORCERER4[level]+1)
                    character.spells4.extend(choose(SORCERER_SPELLS4,q,character.spells4))
                    spellsKnown -= q;
                    self.spell_slots4 = SORCERER4[level]
                if SORCERER3[level]>0:
                    q = random.randrange(1,SORCERER3[level]+1)
                    character.spells3.extend(choose(SORCERER_SPELLS3,q,character.spells3))
                    spellsKnown -= q;
                    self.spell_slots3 = SORCERER3[level]
                if SORCERER2[level]>0:
                    q = random.randrange(1,SORCERER2[level]+1)
                    character.spells2.extend(choose(SORCERER_SPELLS2,q,character.spells2))
                    spellsKnown -= q;
                    self.spell_slots2 = SORCERER2[level]
                self.spell_slots1 = SORCERER1[level]
                q = spellsKnown
                character.spells1.extend(choose(SORCERER_SPELLS1,q,character.spells1)) 
            if self.class_name=="Druid":
                level = str(character.level)
                spellsKnown = character.level+character.get_modifier(character.ability_scores["wisdom"])
                if spellsKnown<1:
                    spellsKnown==1
                character.cantrips.extend(choose(DRUID_CANTRIPS,DRUIDC[level],character.cantrips))
                if DRUID9[level]>0:
                    character.spells9.extend(choose(DRUID_SPELLS9,1,character.spells9))
                    spellsKnown -= 1;
                    self.spell_slots9 = DRUID9[level]
                if DRUID8[level]>0:
                    character.spells8.extend(choose(DRUID_SPELLS8,1,character.spells8))
                    spellsKnown -= 1;
                    self.spell_slots8 = DRUID8[level]
                if DRUID7[level]>0:
                    q = random.randrange(1,DRUID7[level]+1)
                    character.spells7.extend(choose(DRUID_SPELLS7,q,character.spells7))
                    spellsKnown -= q;
                    self.spell_slots7 = DRUID7[level]
                if DRUID6[level]>0:
                    q = random.randrange(1,DRUID6[level]+1)
                    character.spells6.extend(choose(DRUID_SPELLS6,q,character.spells6))
                    spellsKnown -= q;
                    self.spell_slots6 = DRUID6[level]
                if DRUID5[level]>0:
                    q = random.randrange(1,DRUID5[level]+1)
                    character.spells5.extend(choose(DRUID_SPELLS5,q,character.spells5))
                    spellsKnown -= q;
                    self.spell_slots5 = DRUID5[level]
                if DRUID4[level]>0:
                    q = random.randrange(1,DRUID4[level]+2)
                    character.spells4.extend(choose(DRUID_SPELLS4,q,character.spells4))
                    spellsKnown -= q;
                    self.spell_slots4 = DRUID4[level]
                if DRUID3[level]>0:
                    q = random.randrange(1,DRUID3[level]+2)
                    character.spells3.extend(choose(DRUID_SPELLS3,q,character.spells3))
                    spellsKnown -= q;
                    self.spell_slots3 = DRUID3[level]
                if DRUID2[level]>0:
                    q = random.randrange(3,DRUID2[level]+3)
                    character.spells2.extend(choose(DRUID_SPELLS2,q,character.spells2))
                    spellsKnown -= q;
                    self.spell_slots2 = DRUID2[level]
                self.spell_slots1 = DRUID1[level]
                q = spellsKnown
                character.spells1.extend(choose(DRUID_SPELLS1,q,character.spells1))
            if self.class_name=="Cleric":
                level = str(character.level)
                spellsKnown = character.level+character.get_modifier(character.ability_scores["wisdom"])
                if spellsKnown<1:
                    spellsKnown==1
                character.cantrips.extend(choose(CLERIC_CANTRIPS,CLERICC[level],character.cantrips))
                if CLERIC9[level]>0:
                    character.spells9.extend(choose(CLERIC_SPELLS9,1,character.spells9))
                    spellsKnown -= 1;
                    self.spell_slots9 = CLERIC9[level]
                if CLERIC8[level]>0:
                    character.spells8.extend(choose(CLERIC_SPELLS8,1,character.spells8))
                    spellsKnown -= 1;
                    self.spell_slots8 = CLERIC8[level]
                if CLERIC7[level]>0:
                    q = random.randrange(1,CLERIC7[level]+1)
                    character.spells7.extend(choose(CLERIC_SPELLS7,q,character.spells7))
                    spellsKnown -= q;
                    self.spell_slots7 = CLERIC7[level]
                if CLERIC6[level]>0:
                    q = random.randrange(1,CLERIC6[level]+1)
                    character.spells6.extend(choose(CLERIC_SPELLS6,q,character.spells6))
                    spellsKnown -= q;
                    self.spell_slots6 = CLERIC6[level]
                if CLERIC5[level]>0:
                    q = random.randrange(1,CLERIC5[level]+1)
                    character.spells5.extend(choose(CLERIC_SPELLS5,q,character.spells5))
                    spellsKnown -= q;
                    self.spell_slots5 = CLERIC5[level]
                if CLERIC4[level]>0:
                    q = random.randrange(1,CLERIC4[level]+2)
                    character.spells4.extend(choose(CLERIC_SPELLS4,q,character.spells4))
                    spellsKnown -= q;
                    self.spell_slots4 = CLERIC4[level]
                if CLERIC3[level]>0:
                    q = random.randrange(1,CLERIC3[level]+2)
                    character.spells3.extend(choose(CLERIC_SPELLS3,q,character.spells3))
                    spellsKnown -= q;
                    self.spell_slots3 = CLERIC3[level]
                if CLERIC2[level]>0:
                    q = random.randrange(2,CLERIC2[level]+2)
                    character.spells2.extend(choose(CLERIC_SPELLS2,q,character.spells2))
                    spellsKnown -= q;
                    self.spell_slots2 = CLERIC2[level]
                self.spell_slots1 = CLERIC1[level]
                q = spellsKnown
                character.spells1.extend(choose(CLERIC_SPELLS1,q,character.spells1))
            if self.class_name=="Bard":
                level = str(character.level)
                spellsKnown = BARDK[level]
                character.cantrips.extend(choose(BARD_CANTRIPS,BARDC[level],character.cantrips))
                if BARD9[level]>0:
                    character.spells9.extend(choose(BARD_SPELLS9,1,character.spells9))
                    spellsKnown -= 1;
                    self.spell_slots9 = BARD9[level]
                if BARD8[level]>0:
                    character.spells8.extend(choose(BARD_SPELLS8,1,character.spells8))
                    spellsKnown -= 1;
                    self.spell_slots8 = BARD8[level]
                if BARD7[level]>0:
                    q = random.randrange(1,BARD7[level]+1)
                    character.spells7.extend(choose(BARD_SPELLS7,q,character.spells7))
                    spellsKnown -= q;
                    self.spell_slots7 = BARD7[level]
                if BARD6[level]>0:
                    q = random.randrange(1,BARD6[level]+1)
                    character.spells6.extend(choose(BARD_SPELLS6,q,character.spells6))
                    spellsKnown -= q;
                    self.spell_slots6 = BARD6[level]
                if BARD5[level]>0:
                    q = random.randrange(1,BARD5[level]+1)
                    character.spells5.extend(choose(BARD_SPELLS5,q,character.spells5))
                    spellsKnown -= q;
                    self.spell_slots5 = BARD5[level]
                if BARD4[level]>0:
                    q = random.randrange(1,BARD4[level]+2)
                    character.spells4.extend(choose(BARD_SPELLS4,q,character.spells4))
                    spellsKnown -= q;
                    self.spell_slots4 = BARD4[level]
                if BARD3[level]>0:
                    q = random.randrange(1,BARD3[level]+2)
                    character.spells3.extend(choose(BARD_SPELLS3,q,character.spells3))
                    spellsKnown -= q;
                    self.spell_slots3 = BARD3[level]
                if BARD2[level]>0:
                    q = random.randrange(3,BARD2[level]+3)
                    character.spells2.extend(choose(BARD_SPELLS2,q,character.spells2))
                    spellsKnown -= q;
                    self.spell_slots2 = BARD2[level]
                self.spell_slots1 = BARD1[level]
                q = spellsKnown
                character.spells1.extend(choose(BARD_SPELLS1,q,character.spells1))
        if character.level>=2 and self.class_name=="Paladin":
            self.spell_slots9 = ""
            self.spell_slots8 = ""
            self.spell_slots7 = ""
            self.spell_slots6 = ""
            self.spell_slots5 = ""
            self.spell_slots4 = ""
            self.spell_slots3 = ""
            self.spell_slots2 = ""
            self.spell_slots1 = ""
            level = str(character.level)
            spellsKnown = int(math.floor(character.level/2.0))+character.get_modifier(character.ability_scores["charisma"])
            if spellsKnown<1:
                spellsKnown==1
            if PALADIN5[level]>0:
                q = random.randrange(1,PALADIN5[level]+1)
                character.spells5.extend(choose(PALADIN_SPELLS5,q,character.spells5))
                spellsKnown -= q;
                self.spell_slots5 = PALADIN5[level]
            if PALADIN4[level]>0:
                q = random.randrange(1,PALADIN4[level]+1)
                character.spells4.extend(choose(PALADIN_SPELLS4,q,character.spells4))
                spellsKnown -= q;
                self.spell_slots4 = PALADIN4[level]
            if PALADIN3[level]>0:
                q = random.randrange(1,PALADIN3[level]+1)
                character.spells3.extend(choose(PALADIN_SPELLS3,q,character.spells3))
                spellsKnown -= q;
                self.spell_slots3 = PALADIN3[level]
            if PALADIN2[level]>0:
                q = random.randrange(1,PALADIN2[level]+1)
                character.spells2.extend(choose(PALADIN_SPELLS2,q,character.spells2))
                spellsKnown -= q;
                self.spell_slots2 = PALADIN2[level]
            self.spell_slots1 = PALADIN1[level]
            q = spellsKnown
            character.spells1.extend(choose(PALADIN_SPELLS1,q,character.spells1))
            for key in ABILITY_KEYS.keys():
                if ABILITY_KEYS[key]==dclass.spell_casting_ability.lower():
                    self.spell_casting_ability = key
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
        if character.level>=2 and self.class_name=="Ranger":
            self.spell_slots9 = ""
            self.spell_slots8 = ""
            self.spell_slots7 = ""
            self.spell_slots6 = ""
            self.spell_slots5 = ""
            self.spell_slots4 = ""
            self.spell_slots3 = ""
            self.spell_slots2 = ""
            self.spell_slots1 = ""
            level = str(character.level)
            spellsKnown = RANGERK[level]
            if RANGER5[level]>0:
                q = random.randrange(1,RANGER5[level]+1)
                character.spells5.extend(choose(RANGER_SPELLS5,q,character.spells5))
                spellsKnown -= q;
                self.spell_slots5 = RANGER5[level]
            if RANGER4[level]>0:
                q = random.randrange(1,RANGER4[level]+1)
                character.spells4.extend(choose(RANGER_SPELLS4,q,character.spells4))
                spellsKnown -= q;
                self.spell_slots4 = RANGER4[level]
            if RANGER3[level]>0:
                q = random.randrange(1,RANGER3[level]+1)
                character.spells3.extend(choose(RANGER_SPELLS3,q,character.spells3))
                spellsKnown -= q;
                self.spell_slots3 = RANGER3[level]
            if RANGER2[level]>0:
                q = random.randrange(1,RANGER2[level]+1)
                character.spells2.extend(choose(RANGER_SPELLS2,q,character.spells2))
                spellsKnown -= q;
                self.spell_slots2 = RANGER2[level]
            self.spell_slots1 = RANGER1[level]
            q = spellsKnown
            character.spells1.extend(choose(RANGER_SPELLS1,q,character.spells1))
            for key in ABILITY_KEYS.keys():
                if ABILITY_KEYS[key]==dclass.spell_casting_ability.lower():
                    self.spell_casting_ability = key
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            

    #gets features (all features, both general to class and subclass specific, are stored in subclasses
    #this is because most are in subclasses
    #supports all levels though the tool currently only supports level 1
    def get_features(self,character):
        features = []
        features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_1_feature))
        if character.level>=2:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_2_feature))
        if character.level>=3:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_3_feature))
        if character.level>=4:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_4_feature))
        if character.level>=5:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_5_feature))
        if character.level>=6:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_6_feature))
        if character.level>=7:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_7_feature))
        if character.level>=8:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_8_feature))
        if character.level>=9:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_9_feature))
        if character.level>=10:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_10_feature))
        if character.level>=11:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_11_feature))
        if character.level>=12:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_12_feature))
        if character.level>=13:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_13_feature))
        if character.level>=14:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_14_feature))
        if character.level>=15:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_15_feature))
        if character.level>=16:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_16_feature))
        if character.level>=17:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_17_feature))
        if character.level>=18:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_18_feature))
        if character.level>=19:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_19_feature))
        if character.level>=20:
            features.extend(string_to_list(dsubclass.objects.get(name=self.subclass).level_20_feature))
        self.features.extend(features)

    #gives equipment appropriate to class as specified in handbook
    #equipment randomized; either this weapon or that weapon, either this armor or that armor, etc.
    def get_equipment(self, character):
        if self.class_name=="Barbarian":
            if (random.randrange(0,2)==0):
                character.weapons.append("greataxe")
            else:
                x = len(dWeapon.objects.filter(martial_arts=True).filter(mele=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=True).filter(mele=True)[random.randrange(0,x)].weapon_name)
                
            if (random.randrange(0,2)==0):
                character.weapons.append("handaxe")
                self.equipment.append("2 handaxes")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            self.equipment.extend(["explorer's pack", "4 javelins"])
            character.weapons.append("javelin")
            
        if self.class_name=="Bard":
            if (random.randrange(0,3)==0):
                character.weapons.append("rapier")
            elif random.randrange(0,2)==0:
                character.weapons.append("longsword")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
                
            if (random.randrange(0,2)==0):
                self.equipment.append("diplomat's pack")
            else:
                self.equipment.append("entertainer's pack")
            if (random.randrange(0,3)>0):
                self.equipment.append("lute")
            else:
                self.equipment.append(INSTRUMENTS[random.randrange(0,len(INSTRUMENTS))])
            character.armor = "leather"
            character.weapons.append("dagger")
            
        if self.class_name=="Cleric":
            if (random.randrange(0,2)==0):
                character.weapons.append("mace")
            else:
                if "warhammer" in self.proficiencies["weapon"] or "martial" in self.proficiencies["weapon"] or "martial melee" in self.proficiencies["weapon"]:
                    character.weapons.append("warhammer")
                else:
                    character.weapons.append("mace")
            
            if (random.randrange(0,3)==0):
                character.armor = "scale mail"
            elif random.randrange(0,2)==0:
                character.armor = "leather"
            else:
                character.armor = "chain mail"
            if (random.randrange(0,2)==0):
                character.weapons.append("light crossbow")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                character.equipment.append("priest's pack")
            else:
                self.equipment.append("explorer's pack")
            self.equipment.extend(["shield","holy symbol"])

               
        if self.class_name=="Druid":
            if (random.randrange(0,2)==0):
                self.equipment.append("wooden shield")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                character.weapons.append("scimitar")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False).filter(mele=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False).filter(mele=True)[random.randrange(0,x)].weapon_name)
            self.equipment.extend(["explorer's pack","druidic focus"])
            self.armor = "leather"

        if self.class_name=="Fighter":
            if (random.randrange(0,2)==0):
                character.armor = "chain mail"
            else:
                character.armor = "leather"
                character.weapons.append("longbow")
            if (random.randrange(0,2)==0):
                x = len(dWeapon.objects.filter(martial_arts=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=True)[random.randrange(0,x)].weapon_name)
                self.equipment.append("shield")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                 character.weapons.append("light crossbow")
            else:
                character.weapons.append("handaxe")
                self.equipment.append("2 handaxes")
            if (random.randrange(0,2)==0):
                 self.equipment.append("dungeoneer's pack")
            else:
                 self.equipment.append("explorer's pack")

        if self.class_name=="Monk":
            if (random.randrange(0,2)==0):
                character.weapons.append("shortsword")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                 self.equipment.append("dungeoneer's pack")
            else:
                 self.equipment.append("explorer's pack")
            self.equipment.append("ten darts")
            character.weapons.append("dart")
            character.weapons.append("unarmed strike")

        if self.class_name=="Paladin":
            if (random.randrange(0,2)==0):
                x = len(dWeapon.objects.filter(martial_arts=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=True)[random.randrange(0,x)].weapon_name)
                self.equipment.append("shield")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                 character.weapons.append("javelin")
                 self.equipment.append("5 javelins")
            else:
                self.equipment.append("explorer's pack")
            character.armor = "chain mail"
            self.equipment.append("holy symbol")

        if self.class_name=="Ranger":
            if (random.randrange(0,2)==0):
                character.armor = "scale mail"
            else:
                character.armor = "leather"
            if (random.randrange(0,2)==0):
                character.weapons.append("shortsword")
                self.equipment.append("2 shortswords")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False).filter(mele=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False).filter(mele=True)[random.randrange(0,x)].weapon_name)
                x = len(dWeapon.objects.filter(martial_arts=False).filter(mele=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False).filter(mele=True)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                 self.equipment.append("dungeoneer's pack")
            else:
                 self.equipment.append("explorer's pack")
            character.weapons.append("longbow")

        if self.class_name=="Rogue":
            if (random.randrange(0,2)==0):
                character.weapons.append("rapier")
            else:
                character.weapons.append("shortsword")
            if (random.randrange(0,2)==0) and not("shortsword" in character.weapons):
                character.weapons.append("shortsword")
            else:
                character.weapons.append("shortbow")
            if (random.randrange(0,3)==0):
                 self.equipment.append("dungeoneer's pack")
            elif random.randrange(0,2)==0:
                 self.equipment.append("explorer's pack")
            else:
                self.equipment.append("burglar's pack")
            character.weapons.extend(["dagger","dagger"])
            character.armor = "leather"
            self.equipment.append("thieves' tools")

        if self.class_name=="Sorcerer":
            if (random.randrange(0,2)==0):
                character.weapons.append("light crossbow")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                self.equipment.append("component pouch")
            else:
                self.equipment.append("arcane focus")
            if (random.randrange(0,2)==0):
                 self.equipment.append("dungeoneer's pack")
            else:
                self.equipment.append("explorer's pack")
            character.weapons.extend(["dagger","dagger"])

        if self.class_name=="Warlock":
            if (random.randrange(0,2)==0):
                character.weapons.append("light crossbow")
            else:
                x = len(dWeapon.objects.filter(martial_arts=False))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].weapon_name)
            if (random.randrange(0,2)==0):
                self.equipment.append("component pouch")
            else:
                self.equipment.append("arcane focus")
            if (random.randrange(0,2)==0):
                 self.equipment.append("dungeoneer's pack")
            else:
                self.equipment.append("explorer's pack")
            character.weapons.extend(["dagger","dagger"])

        if self.class_name=="Wizard":
            if (random.randrange(0,2)==0):
                character.weapons.append("quarterstaff")
            else:
                character.weapons.append("dagger")
            if (random.randrange(0,2)==0):
                self.equipment.append("component pouch")
            else:
                self.equipment.append("arcane focus")
            if (random.randrange(0,2)==0):
                 self.equipment.append("scholar's pack")
            else:
                self.equipment.append("explorer's pack")
            character.equipment.append("spellbook")


#Race stores the race of the character (Human, Elf, Gnome, Dwarf, etc)
#Race gives ability score increases, languages, some features
class Race:
    def __init__(self, character, name):
        if name=="":
            number_of_records = dRace.objects.count()
            random_index = random.randrange(number_of_records)
            name = dRace.objects.all()[random_index].name
        self.name = name
        character.ability_scores["strength"]+=dRace.objects.get(name=name).str_mod
        character.ability_scores["dexterity"]+=dRace.objects.get(name=name).dex_mod
        character.ability_scores["constitution"]+=dRace.objects.get(name=name).con_mod
        character.ability_scores["intelligence"]+=dRace.objects.get(name=name).int_mod
        character.ability_scores["wisdom"]+=dRace.objects.get(name=name).wis_mod
        character.ability_scores["charisma"]+=dRace.objects.get(name=name).char_mod
        weapons = string_to_list(dRace.objects.get(name=name).weapon_proficiencies.lower())
        armor = string_to_list(dRace.objects.get(name=name).armour_proficiencies.lower())
        tools = string_to_list(dRace.objects.get(name=name).tool_proficiencies.lower())
        #half-elves get plus one to ability scores of choice besides charisma; this randomizes it
        if self.name == "Half-Elf":
            n = 2
            done = []
            for key in character.ability_scores.keys():
                if character.ability_scores[key]%2==1 and character.ability_scores[key]<20 and key!="charisma":
                    character.ability_scores[key]+=1
                    done.append(key)
                    n-=1
                    if n==0:
                        break
            while n>0:
                x = random.randrange(0,6)
                while ABILITY_SCORES[x] in done and character.ability_scores[ABILITY_SCORES[x]]<20 and key!="charisma":
                    x = random.randrange(0,6)
                character.ability_scores[ABILITY_SCORES[x]]+=1
                done.append(ABILITY_SCORES[x])
                n-=1
        #hill dwarves get only one of the possible tool proficiencies; this chooses one
        if self.name == "Dwarf - Hill":
            x = random.randrange(0,len(tools))
            tools = tools[x:x+1]
        skills = string_to_list(dRace.objects.get(name=name).skill_proficiencies.lower())+choose(SKILLS_TOTAL,dRace.objects.get(name=name).optional_skill_proficiencies,character.proficiencies["skill"])
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":[],"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.languages = string_to_list(dRace.objects.get(name=name).language.lower())+choose(LANGUAGES,dRace.objects.get(name=name).optional_lang_proficiencies,character.languages)
        character.languages.extend(self.languages)
        self.base_speed = dRace.objects.get(name=name).speed
        self.features = string_to_list(dRace.objects.get(name=name).features.lower())
        character.features.extend(self.features)
        #certain races get a single cantrip, given below
        if name=="Elf - High":
            x = random.randrange(0,len(WIZARD_CANTRIPS))
            character.cantrips.append(WIZARD_CANTRIPS[x])
            self.spell_casting_ability = "intelligence"
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
        if name=="Gnome - Forest":
            character.cantrips.append("minor illusion")
            self.spell_casting_ability = "intelligence"
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
        if name=="Elf - Dark (Drow)":
            character.cantrips.append("dancing lights")
            self.spell_casting_ability = "charisma"
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
        if name=="Tiefling":
            character.cantrips.append("thaumaturgy")
            self.spell_casting_ability = "charisma"
            self.spell_save_dc = 8+character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])
            self.spell_atk_bonus = character.get_proficiency_bonus()+character.get_modifier(character.ability_scores[self.spell_casting_ability])

#background is where this person came from, what they used to do before adventuring
#this class stores the equipment, proficiencies, and personality traits from your background
class Background:
    def __init__(self, character,name=""):
        if name=="":
            number_of_records = dbackstory.objects.count()
            random_index = random.randrange(number_of_records)
            background = dbackstory.objects.all()[random_index]
            self.name = background.name
        else:
            self.name = name
            background = dbackstory.objects.get(name = self.name)
        self.equipment = string_to_list(background.equipment)
        character.equipment.extend(self.equipment)
        tools = string_to_list(background.tool_proficiencies.lower())
        skills = string_to_list(background.skill_proficiencies.lower())
        self.proficiencies = {"weapon":[],"armor":[],"skill":skills,"saves":[],"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.features = string_to_list(background.feature.lower())
        character.features.extend(self.features)
        self.languages = string_to_list(background.language.lower())+choose(LANGUAGES,background.optional_lang_proficiencies,character.languages)
        character.languages.extend(self.languages)
        self.personality = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.get_personalities()

    #randomly assigns personality traits, bonds, ideals, and flaws from tables in the handbook specific to given background
    def get_personalities(self):
        personality = dpersonalities.objects.get(background=self.name)
        bonds = dbonds.objects.get(background=self.name)
        ideals = dideals.objects.get(background=self.name)
        flaws = dflaws.objects.get(background=self.name)
        a = random.randrange(1,9)
        if a==1:
            self.personality = personality.one
        if a==2:
            self.personality = personality.two
        if a==3:
            self.personality = personality.three
        if a==4:
            self.personality = personality.four
        if a==5:
            self.personality = personality.five
        if a==6:
            self.personality = personality.six
        if a==7:
            self.personality = personality.seven
        if a==8:
            self.personality = personality.eight
        a = random.randrange(1,7)
        if a==1:
            self.bonds = bonds.one
        if a==2:
            self.bonds = bonds.two
        if a==3:
            self.bonds = bonds.three
        if a==4:
            self.bonds = bonds.four
        if a==5:
            self.bonds = bonds.five
        if a==6:
            self.bonds = bonds.six
        a = random.randrange(1,7)
        if a==1:
            self.ideals = ideals.one
        if a==2:
            self.ideals = ideals.two
        if a==3:
            self.ideals = ideals.three
        if a==4:
            self.ideals = ideals.four
        if a==5:
            self.ideals = ideals.five
        if a==6:
            self.ideals = ideals.six
        a = random.randrange(1,7)
        if a==1:
            self.flaws = flaws.one
        if a==2:
            self.flaws = flaws.two
        if a==3:
            self.flaws = flaws.three
        if a==4:
            self.flaws = flaws.four
        if a==5:
            self.flaws = flaws.five
        if a==6:
            self.flaws = flaws.six

#turns string with semicolons into list
def string_to_list(string):
    if string==" " or string=="" or string==None:
        return []
    string = string.replace("; ",";")
    string = string.lower()
    return string.split(";")

#chooses n things from the list l that are not already in l2
def choose(l,n,l2):
    if n==0:
        return []
    index_array = []
    return_array = []
    p = 0
    for k in range(len(l)):
        if l[k] in l2:
            p+=1
    if len(l)-p<n:
        return l
    for i in range(n):
        x = random.randrange(0,len(l))
        while (x in index_array) or (l[x] in l2):
            x = random.randrange(0,len(l))
        index_array.append(x)
        return_array.append(l[x])
    return return_array

#same as choose except if less than n objects of l are not in l2, it only returns n objects, not everything in l
def choosex(l,n,l2):
    if n==0:
        return []
    index_array = []
    return_array = []
    p = 0
    for k in range(len(l)):
        if l[k] in l2:
            p+=1
    if len(l)-p<n:
        for i in range(n):
            x = random.randrange(0,len(l))
            index_array.append(x)
            return_array.append(l[x])
        return return_array
    for i in range(n):
        x = random.randrange(0,len(l))
        while (x in index_array) or (l[x] in l2):
            x = random.randrange(0,len(l))
        index_array.append(x)
        return_array.append(l[x])
    return return_array

#puts + in front of numbers >=0                                        
def pre(x):
    if x>=0:
        return "+" + str(x)
    else:
        return str(x)
