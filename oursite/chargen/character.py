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
    def __init__(self, name, char_class, race, background, ability_scores={"strength":10,"dexterity":10,"constitution":10,"intelligence":10,"wisdom":10,"charisma":10}, level=1):
        self.languages = []
        self.equipment = []
        self.proficiencies = {"weapon":[],"armor":[],"skill":[],"saves":[],"tools":[]}
        self.features = []
        self.weapons = []
        self.armor = ""
        self.level = level
        self.name = name
        self.ability_scores = ability_scores
        self.background = Background(self,background)
        self.my_class = Char_Class(self, char_class, self.level)
        self.my_race = Race(self, race)
        self.skills = {"acrobatics":0,"animal handling":0,"arcana":0,"athletics":0,"deception":0,"history":0,"insight":0,"intimidation":0,"investigation":0,"medicine":0,"nature":0,"perception":0,"performance":0,"persuasion":0,"religion":0,"sleight of hand":0,"stealth":0,"survival":0}
        self.saves = {"strength":0,"dexterity":0,"constitution":0,"intelligence":0,"wisdom":0,"charisma":0}
        [x.lower() for x in self.features]
        self.features = list(set(self.features))
        [x.lower() for x in self.equipment]
        self.equipment = list(set(self.equipment))
        [x.lower() for x in self.languages]
        self.languages = list(set(self.languages))
        for key in self.proficiencies.keys():
            self.proficiencies[key] = list(set(self.proficiencies[key]))

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
        #if (self.my_race.name[0:4]=="Dwar" or self.my_race.name=="Gnome - Rock") and skill=="history":
            #return self.get_modifier(self.ability_scores[RULING_ABILITIES[skill]])+2*self.get_proficiency_bonus()
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
        bonus = 0
        if self.my_race.name=="Dwarf - Hill":
            bonus = self.level
        if self.level==1:
            return self.my_class.hit_die+self.get_modifier(self.ability_scores["constitution"])+bonus
        else:
            return level*(self.my_class.hit_die/2+1+self.get_modifier(self.ability_scores["constitution"]))+bonus

    def get_armor_class(self):
        dex = self.get_modifier(self.ability_scores["dexterity"])
        if self.armor=="":
            if self.my_class.class_name=="Barbarian":
                return 10 + dex + self.get_modifier(self.ability_scores["constitution"])
            if self.my_class.class_name=="Monk":
                return 10 + dex + self.get_modifier(self.ability_scores["wisdom"])
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
        
    
class Char_Class:
    def __init__(self, character, name, level):
        self.class_name = name
        self.subclass = dsubclass.objects.filter(char_class = dChar_class.objects.get(name=self.class_name))[0]
        self.hit_die = dChar_class.objects.get(name=name).hit_die
        weapons = string_to_list(dChar_class.objects.get(name=name).weapon_proficiencies.lower())
        armor = string_to_list(dChar_class.objects.get(name=name).armour_proficiencies.lower())
        tools = string_to_list(dChar_class.objects.get(name=name).tool_proficiencies.lower())
        saves = string_to_list(dChar_class.objects.get(name=name).saving_throws_proficiencies.lower())
        skills = choose(string_to_list(dChar_class.objects.get(name=name).skill_proficiencies),dChar_class.objects.get(name=name).number_skill_proficiencies,character.proficiencies["skill"])
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":saves,"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.equipment = []
        self.get_equipment(character)
        character.equipment.extend(self.equipment)
        self.features = []
        self.get_features(character)
        character.features.extend(self.features)
        self.archetype = Archetype("",level)
        self.languages = []
        character.languages.extend(self.languages)

    def get_features(self,character):
        features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_1_feature)
        if character.level>=2:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_2_feature)
        if character.level>=3:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_3_feature)
        if character.level>=4:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_4_feature)
        if character.level>=5:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_5_feature)
        if character.level>=6:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_6_feature)
        if character.level>=7:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_7_feature)
        if character.level>=8:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_8_feature)
        if character.level>=9:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_9_feature)
        if character.level>=10:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_10_feature)
        if character.level>=11:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_11_feature)
        if character.level>=12:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_12_feature)
        if character.level>=13:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_13_feature)
        if character.level>=14:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_14_feature)
        if character.level>=15:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_15_feature)
        if character.level>=16:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_16_feature)
        if character.level>=17:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_17_feature)
        if character.level>=18:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_18_feature)
        if character.level>=19:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_19_feature)
        if character.level>=20:
            features = string_to_list(dsubclass.objects.get(name=self.subclass.name).level_20_feature)
        self.features.extend(features)


    def get_equipment(self, character):
        if self.class_name=="Barbarian":
            if (random.randrange(0,2)==0):
                character.weapons.append("greataxe")
            else:
                x = len(dWeapon.objects.filter(martial_arts=True).filter(mele=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=True).filter(mele=True)[random.randrange(0,x)].weapon_name)
                
            if (random.randrange(0,2)==0):
                character.weapons.extend(["handaxe","handaxe"])
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
                character.weapons.append(dWeapon.objects.filter(martial_arts=False)[random.randrange(0,x)].name)
            if (random.randrange(0,2)==0):
                character.weapons.append("priest's pack")
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
            self.equipment.append(["explorer's pack","druidic focus"])
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
                 character.weapon.append("light crossbow")
            else:
                character.weapon.extend(["handaxe","handaxe"])
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
            self.weapons.append("dart")

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
                 character.weapon.append("javelin")
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
                character.weapons.extend(["shortsword","shortsword"])
            else:
                x = len(dWeapon.objects.filter(martial_arts=False).filter(mele=True))
                character.weapons.append(dWeapon.objects.filter(martial_arts=False).filter(mele=True)[random.randrange(0,x)].weapon_name)
                x = len(dWeapon.objects.filter(martial_arts=False))
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

        if self.class_name=="Sorceror":
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
"""
Warlock
light crossbow or simple weapon
component pouch or arcane focus
scholar's pack or dungeoneer's pack
leather armor, simple weapon, two daggers

Wizard
quarterstaff or dagger
component pouch or arcane focus
scholar's pack or explorer's pack
spellbook
"""

class Archetype(Char_Class):
    def __init__(self, name, level):
        pass

class Race:
    def __init__(self, character, name):
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
        if self.name == "Dwarf - Hill":
            x = random.randrange(0,len(tools))
            tools = [tools[x:x+1]]
        skills = string_to_list(dRace.objects.get(name=name).skill_proficiencies.lower())+choose(SKILLS_TOTAL,dRace.objects.get(name=name).optional_skill_proficiencies,character.proficiencies["skill"])
        self.proficiencies = {"weapon":weapons,"armor":armor,"skill":skills,"saves":[],"tools":tools}
        for key in self.proficiencies:
            character.proficiencies[key].extend(self.proficiencies[key])
        self.languages = string_to_list(dRace.objects.get(name=name).language.lower())+choose(LANGUAGES,dRace.objects.get(name=name).optional_lang_proficiencies,character.languages)
        character.languages.extend(self.languages)
        self.base_speed = dRace.objects.get(name=name).speed
        self.features = string_to_list(dRace.objects.get(name=name).features.lower())
        character.features.extend(self.features)

class Background:
    def __init__(self, character,name=""):
        if name=="":
            number_of_records = dbackstory.objects.count()
            random_index = random.randrange(number_of_records)
            background = dbackstory.objects.all()[random_index:random_index+1][0]
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
        self.personality_traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""

def string_to_list(string):
    if string==" " or string=="" or string==None:
        return []
    string = string.replace("; ",";")
    string = string.lower()
    return string.split(";")

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


        
