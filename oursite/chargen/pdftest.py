#!python
from fdfgen import forge_fdf
from character import Character
from models import *
import os, subprocess
import random
from django.conf import settings

def fill_pdf(c = Character("Rachel Thorn","Bard","Human","",{"strength":16,"dexterity":10,"constitution":14,"intelligence":8,"wisdom":12,"charisma":8})):
    wpn1 = ""
    wpn1a = ""
    wpn1d = ""
    wpn2 = ""
    wpn2a = ""
    wpn2d = ""
    wpn3 = ""
    wpn3a = ""
    wpn3d = ""
    if len(c.weapons)>0:
        wpn1 = c.weapons[0]
        if dWeapon.objects.get(weapon_name=wpn1).mele==True and not(dWeapon.objects.get(weapon_name=wpn1).finesse==True and c.get_modifier(c.ability_scores["strength"])<c.get_modifier(c.ability_scores["dexterity"])):
            wpn1a = pre(c.get_proficiency_bonus()+c.get_modifier(c.ability_scores["strength"]))
            wpn1d = str(dWeapon.objects.get(weapon_name=wpn1).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=wpn1).type_of_damage_die) + " " + pre(c.get_modifier(c.ability_scores["strength"])) +" " +dWeapon.objects.get(weapon_name=wpn1).damage_type[0] + "."
        else:
            wpn1a = pre(c.get_proficiency_bonus()+c.get_modifier(c.ability_scores["dexterity"]))
            wpn1d = str(dWeapon.objects.get(weapon_name=wpn1).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=wpn1).type_of_damage_die) + " " + pre(c.get_modifier(c.ability_scores["dexterity"])) +" " +dWeapon.objects.get(weapon_name=wpn1).damage_type[0] + "."
        if len(c.weapons)>1:
            wpn2 = c.weapons[1]
            if dWeapon.objects.get(weapon_name=wpn2).mele==True and not(dWeapon.objects.get(weapon_name=wpn2).finesse==True and c.get_modifier(c.ability_scores["strength"])<c.get_modifier(c.ability_scores["dexterity"])):
                wpn2a = pre(c.get_proficiency_bonus()+c.get_modifier(c.ability_scores["strength"]))
                wpn2d = str(dWeapon.objects.get(weapon_name=wpn2).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=wpn2).type_of_damage_die) + " " + pre(c.get_modifier(c.ability_scores["strength"])) +" " +dWeapon.objects.get(weapon_name=wpn2).damage_type[0] + "."
            else:
                wpn2a = pre(c.get_proficiency_bonus()+c.get_modifier(c.ability_scores["dexterity"]))
                wpn2d = str(dWeapon.objects.get(weapon_name=wpn2).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=wpn2).type_of_damage_die) + " " + pre(c.get_modifier(c.ability_scores["dexterity"])) +" " +dWeapon.objects.get(weapon_name=wpn2).damage_type[0] + "."
        if len(c.weapons)>2:
            wpn3 = c.weapons[2]
            if dWeapon.objects.get(weapon_name=wpn3).mele==True and not(dWeapon.objects.get(weapon_name=wpn3).finesse==True and c.get_modifier(c.ability_scores["strength"])<c.get_modifier(c.ability_scores["dexterity"])):
                wpn3a = pre(c.get_proficiency_bonus()+c.get_modifier(c.ability_scores["strength"]))
                wpn3d = str(dWeapon.objects.get(weapon_name=wpn3).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=wpn3).type_of_damage_die) + " " + pre(c.get_modifier(c.ability_scores["strength"])) +" " +dWeapon.objects.get(weapon_name=wpn3).damage_type[0] + "."
            else:
                wpn3a = pre(c.get_proficiency_bonus()+c.get_modifier(c.ability_scores["dexterity"]))
                wpn3d = str(dWeapon.objects.get(weapon_name=wpn3).number_of_damage_die) + "d" + str(dWeapon.objects.get(weapon_name=wpn3).type_of_damage_die) + " " + pre(c.get_modifier(c.ability_scores["dexterity"])) +" " +dWeapon.objects.get(weapon_name=wpn3).damage_type[0] + "."

    fields = [('ClassLevel',str(c.my_class.class_name)+" "+str(c.level)),
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
              ('Passive',c.get_passive_perception()),
              ('ProficienciesLang',list_to_string(c.languages)),
              ('Equipment',list_to_string(c.equipment)),
              ('Features and Traits',list_to_string(c.features)),
              ('Wpn Name',wpn1),
              ('Wpn1 AtkBonus',wpn1a),
              ('Wpn1 Damage',wpn1d),
              ('Wpn Name 2',wpn2),
              ('Wpn2 AtkBonus ',wpn2a),
              ('Wpn2 Damage ',wpn2d),
              ('Wpn Name 3',wpn3),
              ('Wpn3 AtkBonus  ',wpn3a),
              ('Wpn3 Damage ',wpn3d),
              #('PersonalityTraits ',personality),
              #('Bonds',bond),
              #('Flaws',flaw),
              #('Ideals',ideal),
              ]
    fdf = forge_fdf("",fields,[],[],[])
    fdf_file = open("data.fdf","w")
    fdf_file.write(fdf)
    fdf_file.close()
    path = os.path.abspath('..')+'/chargen/myfile.pdf'
    path2 = os.path.abspath('..')+'/data.fdf'
    path3 = os.path.abspath('..')+'/chargen/charactergen.pdf'
    path4 = os.path.abspath('..')+'/chargen/pdftk/bin/pdftk'
    print os.popen(path4+' ' + path + ' fill_form ' + path2 + ' output '+path3)
    """
    pdftk_bin = None
    if pdftk_bin is None:
            from django.conf import settings
            assert hasattr(settings, 'PDFTK_BIN'), "PDF generation requires pdftk (http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/). Edit your PDFTK_BIN settings accordingly."
    pdftk_bin = settings.PDFTK_BIN
    cmd = [
            pdftk_bin,
            src,
            'fill_form',
            '-',
            'output',
            '-',
            'flatten',
        ]
    cmd = ' '.join(cmd)
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE, shell=True)
    
    #subprocess.Popen(["/usr/local/bin/pdftk",path,"fill_form",path2,"output"])
    cmd = [
            settings.PDFTK_BIN,
            path,
            'fill_form',
            path2,
            'output',
            path3,
        ]
    cmd = ' '.join(cmd)
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE, shell=True)

    from subprocess import Popen, PIPE

    cmd = path4+' ' + path +'  fill_form ' + ' '+ path2 + ' output '+ path3
    proc = Popen(cmd,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    cmdout,cmderr = proc.communicate(fdf)
    if cmderr: raise Hppt404
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'inline; filename=mycharacter.pdf'
    response.write(cmdout)
    return response
    """
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
    
