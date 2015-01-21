#!python
from fdfgen import forge_fdf
from character import Character
from models import dWeapon,dpersonalities,dideals,dbonds,dflaws
import os
import random

def fill_pdf(c = Character("Rachel Thorn","Bard","Human",{"strength":16,"dexterity":10,"constitution":14,"intelligence":8,"wisdom":12,"charisma":8})):
    wpn1 = ""
    wpn1a = ""
    wpn1d = ""
    wpn2 = ""
    wpn2a = ""
    wpn2d = ""
    wpn3 = ""
    wpn3a = ""
    wpn3d = ""
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

    a = random.randrange(1,9)
    personality = ""
    if a==1:
        personality = dpersonalities.objects.get(background=c.background.name).one
    elif a==2:
        personality = dpersonalities.objects.get(background=c.background.name).two
    elif a==3:
        personality = dpersonalities.objects.get(background=c.background.name).three
    elif a==4:
        personality = dpersonalities.objects.get(background=c.background.name).four
    elif a==5:
        personality = dpersonalities.objects.get(background=c.background.name).five
    elif a==6:
        personality = dpersonalities.objects.get(background=c.background.name).six
    elif a==7:
        personality = dpersonalities.objects.get(background=c.background.name).seven
    elif a==8:
        personality = dpersonalities.objects.get(background=c.background.name).eight
    a = random.randrange(1,9)
    ideal = ""
    if a==1:
        ideal = dideals.objects.get(background=c.background.name).one
    elif a==2:
        ideal = dideals.objects.get(background=c.background.name).two
    elif a==3:
        ideal = dideals.objects.get(background=c.background.name).three
    elif a==4:
        ideal = dideals.objects.get(background=c.background.name).four
    elif a==5:
        ideal = dideals.objects.get(background=c.background.name).five
    elif a==6:
        ideal = dideals.objects.get(background=c.background.name).six
    print ideal
    a = random.randrange(1,9)
    bond = ""
    if a==1:
        bond = dbonds.objects.get(background=c.background.name).one
    elif a==2:
        bond = dbonds.objects.get(background=c.background.name).two
    elif a==3:
        bond = dbonds.objects.get(background=c.background.name).three
    elif a==4:
        bond = dbonds.objects.get(background=c.background.name).four
    elif a==5:
        bond = dbonds.objects.get(background=c.background.name).five
    elif a==6:
        bond = dideals.objects.get(background=c.background.name).six
    a = random.randrange(1,9)
    flaw = ""
    if a==1:
        flaw = dbonds.objects.get(background=c.background.name).one
    elif a==2:
        flaw = dbonds.objects.get(background=c.background.name).two
    elif a==3:
        flaw = dbonds.objects.get(background=c.background.name).three
    elif a==4:
        flaw = dbonds.objects.get(background=c.background.name).four
    elif a==5:
        flaw = dbonds.objects.get(background=c.background.name).five
    elif a==6:
        flaw = dideals.objects.get(background=c.background.name).six
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
              ('PersonalityTraits ',personality),
              ('Bonds',bond),
              ('Flaws',flaw),
              ('Ideals',ideal),
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

def list_to_string(list):
    string = ""
    for x in list:
        string+=x[0].upper()+x[1:len(x)].lower()+", "
    return string[0:len(string)-2]
    
