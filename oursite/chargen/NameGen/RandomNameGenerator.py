import random
import csv

def randomname(race):
    names = []
    namespre = []
    namesmid = []
    namesend = []
    if race=="Dwarf - Hill" or race=="Dwarf - Mountain":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/DwarfMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/DwarfMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/DwarfFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/DwarfFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Elf - High" or race=="Elf - Wood":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/ElfMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/ElfMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/ElfFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/ElfFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Elf - Dark (Drow)":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/DrowMale.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    names.append(row)
        else:
            with open('chargen/NameGen/DrowFemale.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    names.append(row)
    elif race=="Halfling - Lightfoot" or race=="Halfling - Stout":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/HalflingMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/HalflingMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/HalflingFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/HalflingFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Dragonborn":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/DragonbornMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/DragonbornMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/DragonbornFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/DragonbornFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Gnome - Forest" or race=="Gnome - Rock":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/GnomeMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/GnomeMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/GnomeFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/GnomeFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Half-Elf":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/HalfElfMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/HalfElfMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/HalfElfFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/HalfElfFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Half-Orc":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/HalfOrcMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/HalfOrcMaleMid.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesmid.append(row)
            with open('chargen/NameGen/HalfOrcMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/HalfOrcFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/HalfOrcFemaleMid.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesmid.append(row)
            with open('chargen/NameGen/HalfOrcFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    elif race=="Tiefling":
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/TieflingMalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/TieflingMaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
        else:
            with open('chargen/NameGen/TieflingFemalePre.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namespre.append(row)
            with open('chargen/NameGen/TieflingFemaleEnd.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    namesend.append(row)
    else:
        if random.randrange(0,2)==0:
            with open('chargen/NameGen/HumanMale.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    names.append(row)
        else:
            with open('chargen/NameGen/HumanFemale.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',')
                for row in spamreader:
                    names.append(row)
    if len(namesmid)>0:
        return namespre[0][random.randrange(0,len(namespre[0]))]+namesmid[0][random.randrange(0,len(namesmid[0]))]+namesend[0][random.randrange(0,len(namesend[0]))]
    elif len(namespre)>0:
        return namespre[0][random.randrange(0,len(namespre[0]))]+namesend[0][random.randrange(0,len(namesend[0]))]
    else:
        return names[0][random.randrange(0,len(names[0]))]

print randomname("Human")
