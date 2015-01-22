#!python
from fdfgen import forge_fdf
from character import Character
import os, subprocess, platform
import random
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader

def fill_pdf(c = Character("Rachel Thorn","Bard","Human","",16,10,14,8,12,8)):
    c11 = "Off"
    c18 = "Off"
    c19 = "Off"
    c20 = "Off"
    c21 = "Off"
    c22 = "Off"
    if "str" in c.proficiencies["saves"]:
        c11 = "Yes" 
    if "dex" in c.proficiencies["saves"]:
        c18 = "Yes" 
    if "con" in c.proficiencies["saves"]:
        c19 = "Yes" 
    if "int" in c.proficiencies["saves"]:
        c20 = "Yes" 
    if "wis" in c.proficiencies["saves"]:
        c21 = "Yes" 
    if "char" in c.proficiencies["saves"]:
        c22 = "Yes" 
    c23 = "Off"
    c24 = "Off"
    c25 = "Off"
    c26 = "Off"
    c27 = "Off"
    c28 = "Off"
    c29 = "Off"
    c30 = "Off"
    c31 = "Off"
    c32 = "Off"
    c33 = "Off"
    c34 = "Off"
    c35 = "Off"
    c36 = "Off"
    c37 = "Off"
    c38 = "Off"
    c39 = "Off"
    c40 = "Off"
    if "acrobatics" in c.proficiencies["skill"]:
        c23 = "Yes"
    if "animal handling" in c.proficiencies["skill"]:
        c24 = "Yes"
    if "arcana" in c.proficiencies["skill"]:
        c25 = "Yes"
    if "athletics" in c.proficiencies["skill"]:
        c26 = "Yes"
    if "deception" in c.proficiencies["skill"]:
        c27 = "Yes"
    if "history" in c.proficiencies["skill"]:
        c28 = "Yes"
    if "insight" in c.proficiencies["skill"]:
        c29 = "Yes"
    if "intimidation" in c.proficiencies["skill"]:
        c30 = "Yes"
    if "investigation" in c.proficiencies["skill"]:
        c31 = "Yes"
    if "medicine" in c.proficiencies["skill"]:
        c32 = "Yes"
    if "nature" in c.proficiencies["skill"]:
        c33 = "Yes"
    if "perception" in c.proficiencies["skill"]:
        c34 = "Yes"
    if "performance" in c.proficiencies["skill"]:
        c35 = "Yes"
    if "persuasion" in c.proficiencies["skill"]:
        c36 = "Yes"
    if "religion" in c.proficiencies["skill"]:
        c37 = "Yes"
    if "sleight of hand" in c.proficiencies["skill"]:
        c38 = "Yes"
    if "stealth" in c.proficiencies["skill"]:
        c39 = "Yes"
    if "survival" in c.proficiencies["skill"]:
        c40 = "Yes"
    fields = [('ClassLevel',str(c.my_class.class_name)+" "+str(c.level)),
              ('CharacterName',c.name),
              ('Background',c.background.name),
              ('Race ',c.my_race.name),
              ('STR',c.ability_scores["strength"]),
              ('ProfBonus',pre(c.get_proficiency_bonus())),
              ('Initiative',pre(c.get_initiative())),
              ('AC',c.get_armor_class()),
              ('Speed',c.my_race.base_speed),
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
              ('HDTotal',str(c.level)+"d"+str(c.my_class.hit_die)),
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
              ('Passive',c.get_passive_perception()),
              ('ProficienciesLang',list_to_string(c.languages)),
              ('Equipment',list_to_string(c.equipment)),
              ('Features and Traits',list_to_string(c.features)),
              ('Wpn Name',c.wpn1),
              ('Wpn1 AtkBonus',c.wpn1a),
              ('Wpn1 Damage',c.wpn1d),
              ('Wpn Name 2',c.wpn2),
              ('Wpn2 AtkBonus ',c.wpn2a),
              ('Wpn2 Damage ',c.wpn2d),
              ('Wpn Name 3',c.wpn3),
              ('Wpn3 AtkBonus  ',c.wpn3a),
              ('Wpn3 Damage ',c.wpn3d),
              ('PersonalityTraits ',c.background.personality),
              ('Bonds',c.background.bonds),
              ('Flaws',c.background.flaws),
              ('Ideals',c.background.ideals),
              ('Check Box 23',c23),
              ('Check Box 24',c24),
              ('Check Box 25',c25),
              ('Check Box 26',c26),
              ('Check Box 27',c27),
              ('Check Box 28',c28),
              ('Check Box 29',c29),
              ('Check Box 30',c30),
              ('Check Box 31',c31),
              ('Check Box 32',c32),
              ('Check Box 33',c33),
              ('Check Box 34',c34),
              ('Check Box 35',c35),
              ('Check Box 36',c36),
              ('Check Box 37',c37),
              ('Check Box 38',c38),
              ('Check Box 39',c39),
              ('Check Box 40',c40),
              ('Check Box 11',c11),
              ('Check Box 18',c18),
              ('Check Box 19',c19),
              ('Check Box 20',c20),
              ('Check Box 21',c21),
              ('Check Box 22',c22),
              ]
    character2 = os.path.abspath('..')+'/oursite/chargen/myfile2.pdf'
    pdftk = os.path.abspath('..')+'/oursite/chargen/pdftk/bin/pdftk'
    if platform.system()=='Windows':
        pdftk = os.path.abspath('..')+'/oursite/chargen/pdftkserver/bin/pdftk.exe'
    spellcastingclasses = ["Druid","Cleric","Bard","Wizard","Sorcerer","Warlock"]
    if (c.level==1):
        if c.my_class.class_name in spellcastingclasses:
            fields2 = [('Spellcasting Class 2',c.my_class.class_name),
                       ('SpellcastingAbility 2',c.my_class.spell_casting_ability),
                       ]
            fdf = forge_fdf("",fields2,[],[],[])
            path = os.path.abspath('..')+'/oursite/chargen/data2.fdf'
            fdf_file = open(path,"w")
            fdf_file.write(fdf)
            fdf_file.close()
            data2 = os.path.abspath('..')+'/oursite/chargen/data2.fdf'
            character2 = os.path.abspath('..')+'/oursite/chargen/character2.pdf'
            myfile2 = os.path.abspath('..')+'/oursite/chargen/myfile2.pdf'
            os.system(pdftk+' ' + myfile2 + ' fill_form ' + data2 + ' output '+character2)
    fdf = forge_fdf("",fields,[],[],[])
    path = os.path.abspath('..')+'/oursite/chargen/data.fdf'
    fdf_file = open(path,"w")
    fdf_file.write(fdf)
    fdf_file.close()

    
    
    myfile = os.path.abspath('..')+'/oursite/chargen/myfile.pdf'
    data = os.path.abspath('..')+'/oursite/chargen/data.fdf'
    character1 = os.path.abspath('..')+'/oursite/chargen/character1.pdf'
    pdftk = os.path.abspath('..')+'/oursite/chargen/pdftkserver/bin/pdftk.exe'
    myfile2 = os.path.abspath('..')+'/oursite/chargen/myfile2.pdf'
    charactergen = os.path.abspath('..')+'/oursite/chargen/charactergen.pdf'
    myfile3 = os.path.abspath('..')+'/oursite/chargen/myfile3.pdf'

    os.system(pdftk+' ' + myfile + ' fill_form ' + data + ' output '+character1)
    os.system(pdftk + ' ' + character1 + ' ' + myfile3 + ' ' + character2 + ' cat output ' + charactergen)
    with open(charactergen, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        filename = c.name+"_character_sheet.pdf"
        response['Content-Disposition'] = 'inline; filename='+filename
        return response
    

    
def pre(x):
    if x>0:
        return "+" + str(x)
    else:
        return str(x)

def list_to_string(list):
    string = ""
    for x in list:
        string+=x[0].upper()+x[1:len(x)].lower()+", "
    return string[0:len(string)-2]
    
