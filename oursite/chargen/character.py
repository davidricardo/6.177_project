#stores Character objects
import math

import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from models import *
TEST_MESSAGE = "HELLO? Rachel put in this test message text in character.py."

#splitting up long lists and dicts like this makes them much easier to read,
#plus it gets rid of obnoxiously long lines and you can easily collapse them.
RULING_ABILITIES = {
    "acrobatics": "dexterity",
    "animal handling":" wisdom",
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
        self.level = level
        self.name = name
        self.ability_scores = ability_scores
        self.my_class = Char_Class(self, char_class, self.level)
        self.my_race = Race(self, race, self.level)
        self.background = Background()
        self.skills = {"acrobatics":0,"animal handling":0,"arcana":0,"athletics":0,"deception":0,"history":0,"insight":0,"intimidation":0,"investigation":0,"medicine":0,"nature":0,"perception":0,"performance":0,"persuasion":0,"religion":0,"sleight of hand":0,"stealth":0,"survival":0}
        self.saves = {"strength":0,"dexterity":0,"constitution":0,"intelligence":0,"wisdom":0,"charisma":0}
        
        for s in skills.keys():
            skills[s] = calculate_skill(s)
        for v in saves.keys():
            saves[v] = calculate_save(v)

def get_proficiencies(self):
    proficiencies = {"weapon":[],"armor":[],"skill":[],"saves":[],"tools":[]}
        for key in proficiencies.keys():
            proficiencies[key] = list(set(self.my_class.proficiencies[key].append(self.my_class.my_race.proficiencies[key].append(self.background.proficiencies[key]))))
    return proficiencies

def get_equipment(self):
    return list(set(self.my_class.equipment.append(self.background.equipment)))
    
    def get_languages(self):
        return list(set(self.my_class.languages.append(self.background.languages.append(self.my_race.languages))))
    
    def get_features(self):
        return list(set(self.my_class.features.append(self.background.langugaes.append(self.my_race.languages))))
    
    #returns proficiency bonus, calculated from level
    def get_proficiency_bonus(self):
        return int(1+math.ceil(self.level/4.0))
    
    #returns modifier on ability score
    def get_modifier(self, score):
        return int(math.floor((score-10)/2.0))
    
    #returns initiative modifier (just the dex modifier)
    def get_initiative(self):
        return get_modifier(self.ability_scores["dexterity"])
    
    #calculates skills from ruling abilities and proficiencies
    def calculate_skill(self,skill):
        if skill in get_proficiencies()["skill"]:
            return get_modifier(self.ability_scores[RULING_ABILITIES[skill]])+get_proficiency_bonus()
        else:
            return get_modifier(self.ability_scores[RULING_ABILITIES[skill]])

#calculates saves from abilities and proficiencies
def calculate_save(self,save):
    if save in get_proficiencies()["saves"]:
        return get_modifier(self.ability_scores[save])+get_proficiency_bonus()
        else:
            return get_modifier(self.ability_scores[save])
                
                def get_max_hit_points(self):
                    if self.level==1:
return self.my_class.hit_die+get_modifier(self.ability_scores["constitution"])
    else:
        return level*(self.my_class.hit_die/2+1+get_modifier(self.ability_scores["constitution"]))

class Char_Class:
    def __init__(self, character, name, level):
        self.class_name = name
        self.hit_die = job.objects.get(name=name).hit_die
        weapons = string_to_list(job.objects.get(name=name).weapon_proficiencies)
        armor = string_to_list(job.objects.get(name=name).armour_proficiencies)
        tools = string_to_list(job.objects.get(name=name).tool_proficiencies)
        saves = string_to_list(job.objects.get(name=name).saving_throws__proficiencies)
        skills = string_to_list(job.objects.get(name=name).skill_proficiencies)
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":saves,"tools":tools}
        self.equipment = []
        self.features = string_to_list(job.objects.get(name=name).features)
        self.archetype = Archetype("",level)
        self.languages = []

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
        skills = string_to_list(Char_Race.objects.get(name=name).skill_proficiencies)
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":[],"tools":tools}
        self.languages = string_to_list(Char_Race.objects.get(name=name).language)
        self.base_speed = Char_Race.objects.get(name=name).speed
        self.features = string_to_list(Char_Race.objects.get(name=name).features)

class Subrace(Race):
    def __init__(self):
        pass

class Background:
    def __init__(self):
        self.equipment = []
        self.proficiencies = {"weapon":[],"armor":[],"skill":[],"saves":[],"tools":[]}
        self.features = []
        self.languages = []
        self.personality_traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""

def string_to_list(string):
    string = string.replace(", ",",")
    string = string.lower()
    return string.split(",")
