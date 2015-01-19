#stores Character objects
import math, random

import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from models import *
from collections import OrderedDict

#splitting up long lists and dicts like this makes them much easier to read,
#plus it gets rid of obnoxiously long lines and you can easily collapse them.
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

ABILITY_KEYS = {"strength":"str",
                "dexterity":"dex",
                "constitution":"con",
                "intelligence":"int",
                "wisdom":"wis",
                "charisma":"char"}

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

#this dictionary includes everything that will be passed to the user.
# its entries should take the form of "<variable name>": <varible value>.
VARS_TO_PASS = {
    # "test_message" : Weapon.objects.all()
    "starting_ability_scores" : {
        "strength" : 8,
        "dexterity" : 8,
        "constitution" : 8,
        "intelligence" : 8,
        "wisdom" : 8,
        "charisma" : 8
        }
}



class Character:
    def __init__(self, name, char_class, race, ability_scores={"strength":10,"dexterity":10,"constitution":10,"intelligence":10,"wisdom":10,"charisma":10}, level=1):
        self.languages = []
        self.equipment = []
        self.proficiencies = {"weapon":[],"armor":[],"skill":[],"saves":[],"tools":[]}
        self.features = []
        self.level = level
        self.name = name
        self.ability_scores = ability_scores
        self.my_class = Char_Class(self, char_class, self.level)
        self.my_race = Race(self, race)
        self.background = Background()
        self.skills = {"acrobatics":0,"animal handling":0,"arcana":0,"athletics":0,"deception":0,"history":0,"insight":0,"intimidation":0,"investigation":0,"medicine":0,"nature":0,"perception":0,"performance":0,"persuasion":0,"religion":0,"sleight of hand":0,"stealth":0,"survival":0}
        self.saves = {"strength":0,"dexterity":0,"constitution":0,"intelligence":0,"wisdom":0,"charisma":0}
        
        for s in self.skills.keys():
            self.skills[s] = self.calculate_skill(s)
        for v in self.saves.keys():
            self.saves[v] = self.calculate_save(v)

    def get_final_dict(self):
        my_dict = OrderedDict()
        my_dict["Name"]=self.name,
        my_dict["Level"]=self.level,
        my_dict["Race"]=self.my_race.name,
        my_dict["Class"]=self.my_class.class_name,
        my_dict["Background"]=self.background.name,
        my_dict["Proficiency Bonus"]=self.get_proficiency_bonus(),
        
        for key in self.ability_scores.keys():
            #capitalizes ability scores, i.e, "Strength" and "Strength modifier"
            my_dict[key[0].upper()+key[1:len(key)]]=self.ability_scores[key]
            my_dict[key[0].upper()+key[1:len(key)]+" Modifier"]=self.get_modifier(self.ability_scores[key])
        my_dict["Initiative"] = self.get_initiative()
        my_dict["Max Hit Points"] = self.get_max_hit_points()
        my_dict["Hit Die"] = str(self.level)+"d"+str(self.my_class.hit_die)
        my_dict["Speed"] = self.my_race.base_speed
        for key in self.saves.keys():
            my_dict[key[0].upper()+key[1:len(key)]+" Save"]=self.saves[key]
        for key in self.skills.keys():
            my_dict[key[0].upper()+key[1:len(key)]]=self.skills[key]
        my_dict["Equipment"]=', '.join(self.get_equipment())
        my_dict["Languages"]=', '.join(self.get_languages())
        my_dict["Features"]=', '.join(self.get_features())
        return my_dict

    def get_passive_perception(self):
        return 10+self.skills["perception"]
    
    #returns proficiency bonus, calculated from level
    def get_proficiency_bonus(self):
        return int(1+math.ceil(self.level/4.0))
    
    #returns modifier on ability score
    def get_modifier(self, score):
        return int(math.floor((score-10)/2.0))
    
    #returns initiative modifier (just the dex modifier)
    def get_initiative(self):
        return self.get_modifier(self.ability_scores["dexterity"])
    
    #calculates skills from ruling abilities and proficiencies
    def calculate_skill(self,skill):
        if skill in self.proficiencies["skill"]:
            return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])+self.get_proficiency_bonus()
        else:
            return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])

    #calculates saves from abilities and proficiencies
    def calculate_save(self,save):
        if save in self.proficiencies["saves"]:
            return self.get_modifier(self.ability_scores[save])+self.get_proficiency_bonus()
        elif ABILITY_KEYS[save] in self.proficiencies["saves"]:
            return self.get_modifier(self.ability_scores[save])+self.get_proficiency_bonus()
        else:
            return self.get_modifier(self.ability_scores[save])
                
    def get_max_hit_points(self):
        if self.level==1:
            return self.my_class.hit_die+self.get_modifier(self.ability_scores["constitution"])
        else:
            return level*(self.my_class.hit_die/2+1+self.get_modifier(self.ability_scores["constitution"]))

    def get_armor_class(self):
        return 0
    
class Char_Class:
    def __init__(self, character, name, level):
        self.class_name = name
        self.hit_die = job.objects.get(name=name).hit_die
        weapons = string_to_list(job.objects.get(name=name).weapon_proficiencies)
        armor = string_to_list(job.objects.get(name=name).armour_proficiencies)
        tools = string_to_list(job.objects.get(name=name).tool_proficiencies)
        saves = string_to_list(job.objects.get(name=name).saving_throws_proficiencies)
        skills = choose(string_to_list(job.objects.get(name=name).skill_proficiencies),job.objects.get(name=name).number_skill_proficiencies,character.proficiencies["skill"])
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":saves,"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.equipment = []
        character.equipment.extend(self.equipment)
        self.features = string_to_list(job.objects.get(name=name).features)
        character.features.extend(self.features)
        self.archetype = Archetype("",level)
        self.languages = []
        character.languages.extend(self.languages)

class Archetype(Char_Class):
    def __init__(self, name, level):
        pass

class Race:
    def __init__(self, character, name):
        self.name = name
        character.ability_scores["strength"]+=Char_Race.objects.get(name=name).str_mod
        character.ability_scores["dexterity"]+=Char_Race.objects.get(name=name).dex_mod
        character.ability_scores["constitution"]+=Char_Race.objects.get(name=name).con_mod
        character.ability_scores["intelligence"]+=Char_Race.objects.get(name=name).int_mod
        character.ability_scores["wisdom"]+=Char_Race.objects.get(name=name).wis_mod
        character.ability_scores["charisma"]+=Char_Race.objects.get(name=name).char_mod
        weapons = string_to_list(Char_Race.objects.get(name=name).weapon_proficiencies)
        armor = string_to_list(Char_Race.objects.get(name=name).armour_proficiencies)
        tools = string_to_list(Char_Race.objects.get(name=name).tool_proficiencies)
        skills = string_to_list(Char_Race.objects.get(name=name).skill_proficiencies)+choose(SKILLS_TOTAL,Char_Race.objects.get(name=name).optional_skill_proficiencies,character.proficiencies["skill"])
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":[],"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.languages = string_to_list(Char_Race.objects.get(name=name).language)+choose(LANGUAGES,Char_Race.objects.get(name=name).optional_lang_proficiencies,character.languages)
        character.languages.extend(self.languages)
        self.base_speed = Char_Race.objects.get(name=name).speed
        self.features = string_to_list(Char_Race.objects.get(name=name).features)
        character.features.extend(self.features)

class Background:
    def __init__(self):
        self.name = ""
        self.equipment = []
        self.proficiencies = {"weapon":[],"armor":[],"skill":[],"saves":[],"tools":[]}
        self.features = []
        self.languages = []
        self.personality_traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""

def string_to_list(string):
    if string==" " or string=="" or string==None:
        return []
    string = string.replace(", ",",")
    string = string.lower()
    return string.split(",")

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


        
