#!python
# YOU SHOULD DOWNLOAD PDFtk Server https://www.pdflabs.com/tools/pdftk-server/
from fdfgen import forge_fdf
from character import Character
from django.http import HttpResponse
import subprocess, os

def fill_pdf(c = Character("Rachel","Barbarian","Dwarf - Hill",{"strength":8,"dexterity":12,"constitution":10,"intelligence":18,"wisdom":14,"charisma":10})):
    fields = [('ClassLevel',c.my_class.class_name+" "+str(c.level)),
              ('CharacterName',c.name),
              ('Background',c.background.name),
              ('Race ',c.my_race.name),
              ('STR',c.ability_scores["strength"]),
              ('ProfBonus',pre(c.get_proficiency_bonus())),
              ('Initiative',pre(c.get_initiative())),
              ('AC',c.get_armor_class()),
              ('Speed',c.my_race.base_speed),
              ('PersonalityTraits',c.background.personality_traits),
              ('STRmod',pre(c.get_modifier(c.ability_scores["strength"]))),
              ('HPMax',c.get_max_hit_points()),
              ('ST Strength',pre(c.saves["strength"])),
              ('DEX',c.ability_scores["dexterity"]),
              ('DEXmod ',pre(c.get_modifier(c.ability_scores["dexterity"]))),
              ('ST Dexterity',pre(c.saves["dexterity"])),
              ('CON',c.ability_scores["constitution"]),
              ('CONmod',pre(c.get_modifier(c.ability_scores["constitution"]))),
              ('ST Constitution',pre(c.saves["constitution"])),
              ('INT',c.ability_scores["intelligence"]),
              ('INTmod',pre(c.get_modifier(c.ability_scores["intelligence"]))),
              ('ST Intelligence',pre(c.saves["intelligence"])),
              ('WIS',c.ability_scores["wisdom"]),
              ('WISmod',pre(c.get_modifier(c.ability_scores["wisdom"]))),
              ('ST Wisdom',pre(c.saves["wisdom"])),
              ('CHA',c.ability_scores["charisma"]),
              ('CHamod',pre(c.get_modifier(c.ability_scores["charisma"]))),
              ('ST Charisma',pre(c.saves["charisma"])),
              ('Ideals',c.background.ideals),
              ('Bonds',c.background.bonds),
              ('HDTotal',str(c.level)+"d"+str(c.my_class.hit_die)),
              ('Flaws',c.background.flaws),
              ('Acrobatics',pre(c.skills["acrobatics"])),
              ('Animal',pre(c.skills["animal handling"])),
              ('Athletics',pre(c.skills["athletics"])),
              ('Deception ',pre(c.skills["deception"])),
              ('History ',pre(c.skills["history"])),
              ('Insight',pre(c.skills["insight"])),
              ('Intimidation',pre(c.skills["intimidation"])),
              ('Investigation ',pre(c.skills["investigation"])),
              ('Arcana',pre(c.skills["arcana"])),
              ('Perception ',pre(c.skills["perception"])),
              ('Performance',pre(c.skills["performance"])),
              ('Nature',pre(c.skills["nature"])),
              ('Medicine',pre(c.skills["medicine"])),
              ('Religion',pre(c.skills["religion"])),
              ('Stealth ',pre(c.skills["stealth"])),
              ('Persuasion',pre(c.skills["persuasion"])),
              ('SleightofHand',pre(c.skills["sleight of hand"])),
              ('Survival',pre(c.skills["survival"])),
              ('Passive',c.get_passive()),
              ('ProficienciesLang',c.get_languages()),
              ('Equipment',c.get_equipment()),
              ('Features and Traits',c.get_features())
              ]
    fdf = forge_fdf("",fields,[],[],[])
    fdf_file = open("data.fdf","wb")
    fdf_file.write(fdf)
    fdf_file.close()
    path = os.path.abspath('..')+'/chargen/myfile.pdf'
    path2 = os.path.abspath('..')+'/chargen/data.fdf'
    path3 = os.path.abspath('..')+'/chargen/charactergen.pdf'
    os.system('/usr/local/bin/pdftk ' + path + ' fill_form ' + path2 + ' output '+path3)
    
def pre(x):
    if x>0:
        return "+" + str(x)
    else:
        return str(x)
