#stores Character objects
import math

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


class Character:
    def __init__(self, name, char_class, race, ability_scores = {"strength":10,"dexterity":10,"constitution":10,"intelligence":10,"wisdom":10,"charisma":10}, level=1):
        self.level = level
        self.name = name
        self.my_class = Char_Class(char_class, self.level)
        self.my_race = Race(race, self.level)
        self.background = Background() 
        self.skills = {
            "acrobatics": 0,
            "animal handling": 0,
            "arcana": 0,
            "athletics": 0,
            "deception": 0,
            "history": 0,
            "insight": 0,
            "intimidation": 0,
            "investigation": 0,
            "medicine": 0,
            "nature": 0,
            "perception": 0,
            "performance": 0,
            "persuasion": 0,
            "religion": 0,
            "sleight of hand": 0,
            "stealth": 0,
            "survival": 0
        }
        self.saves = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        }
        self.ability_scores = ability_scores

        for s in skills.keys():
            skills[s] = calculate_skill(s)
        for v in saves.keys():
            saves[v] = calculate_save(v)
            
    def get_proficiencies(self):
        proficiencies = {
            "weapon": [],
            "armor": [],
            "skill": [],
            "saves": [],
            "tools": []
            }

        for key in proficiencies.keys():
            #list(set()) removes duplicates from the list
            proficiencies[key] = list( set( 
                self.my_class.proficiencies[key].append(
                    self.my_class.my_race.proficiencies[key].append(
                        self.background.proficiencies[key]
                    )
                )
            ))
        return proficiencies

    def get_equipment(self):
        return list( set( 
            self.my_class.equipment.append(
                self.background.equipment
                )
            ))

    def get_languages(self):
        return list( set( 
            self.my_class.languages.append(
                self.background.languages.append(
                    self.my_race.languages
                    )
                )
            ))

    def get_features(self):
        return list( set( 
            self.my_class.features.append(
                self.background.langugaes.append(
                    self.my_race.languages
                    )
                )
            ))
        
    def get_proficiency_bonus(self):
        #returns proficiency bonus, calculated from level
        #isn't proficiency bonus +2 at first level?
        return int( 1 + math.ceil( self.level / 4.0 ))

    def get_modifier(self, score):
        #returns modifier on ability score
        return int( math.floor( (score - 10) / 2.0 ))

    def get_initiative(self):
        #returns initiative modifier (just the dex modifier)

        #once feats are implemented, this should also check to  
        #see if the character has the Alert feat and if so add 5.
        return get_modifier(
            self.ability_scores["dexterity"]
        )

    def calculate_skill(skill):
        #calculates skills from ruling abilities and proficiencies
        skill_modifier = get_modifier(
            self.ability_scores[
                    RULING_ABILITIES[skill]
                ]
            )

        if skill in get_proficiencies()["skill"]:
            skill_modifier += get_proficiency_bonus()

        return skill_modifier

    def calculate_save(save):
        #calculates saves from abilities and proficiencies
        save_modifier = get_modifier(
            self.ability_scores[save]
        )

        if save in get_proficiencies()["saves"]:
            save_modifier += get_proficiency_bonus()
        
        return save_modifier
            

class Char_Class:
    def __init__(self, name, level):
        self.class_name = name
        self.hit_die = 0
        self.hit_max = 0
        self.proficiencies = {
            "weapon": [],
            "armor": [],
            "skill": [],
            "saves": [],
            "tools": []
            }
        self.equipment = []
        self.features = []
        self.archetype = Archetype("",level)
        self.speed_modifier = 0
        self.languages = []

class Archetype(Char_Class):
    def __init__(self, name, level):
        pass
    
class Race:
   def __init__(self, name):
       self.proficiencies = {
           "weapon": [],
           "armor": [],
           "skill": [],
           "saves": [],
           "tools": []
            }
       self.languages = []
       self.base_speed = 0
       self.features = []

class Subrace(Race):
    def __init__(self):
        pass
        
class Background:
    def __init__(self):
        self.equipment = []
        self.proficiencies = {
            "weapon": [],
            "armor": [],
            "skill": [],
            "saves": [],
            "tools": []
            }

        self.features = []
        self.languages = []
        self.personality_traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""

class Weapon:
    def __init__(self):
        pass
