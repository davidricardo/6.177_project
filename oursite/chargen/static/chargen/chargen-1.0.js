document.title = "D&D 5E Character Generator"
window.onload = function(){
    console.log ("window ready");

            //This object contains variable names for all the useful elements on the page.
        var elements = {
            //These are indented so you can collapse them.
            strength_total_box : document.getElementById("total_strength_score"),
                dexterity_total_box : document.getElementById("total_dexterity_score"),
                constitution_total_box : document.getElementById("total_constitution_score"),
                intelligence_total_box : document.getElementById("total_intelligence_score"),
                wisdom_total_box : document.getElementById("total_wisdom_score"),
                charisma_total_box : document.getElementById("total_charisma_score"),

            strength_mod_box : document.getElementById("total_strength_mod"),
                dexterity_mod_box : document.getElementById("total_dexterity_mod"),
                constitution_mod_box : document.getElementById("total_constitution_mod"),
                intelligence_mod_box : document.getElementById("total_intelligence_mod"),
                wisdom_mod_box : document.getElementById("total_wisdom_mod"),
                charisma_mod_box : document.getElementById("total_charisma_mod"),

            strength_from_pb_box : document.getElementById("id_strength"),
                dexterity_from_pb_box : document.getElementById("id_dexterity"),
                constitution_from_pb_box : document.getElementById("id_constitution"),
                intelligence_from_pb_box : document.getElementById("id_intelligence"),
                wisdom_from_pb_box : document.getElementById("id_wisdom"),
                charisma_from_pb_box : document.getElementById("id_charisma"),
        };

        console.log(elements.strength_from_pb_box.options[elements.strength_from_pb_box.selectedIndex].value);
        elements.dexterity_from_pb = elements.dexterity_from_pb_box.options[elements.dexterity_from_pb_box.selectedIndex].value;
        elements.constitution_from_pb = elements.constitution_from_pb_box.options[elements.constitution_from_pb_box.selectedIndex].value;
        elements.intelligence_from_pb = elements.intelligence_from_pb_box.options[elements.intelligence_from_pb_box.selectedIndex].value;
        elements.wisdom_from_pb = elements.wisdom_from_pb_box.options[elements.wisdom_from_pb_box.selectedIndex].value;
        elements.charisma_from_pb = elements.charisma_from_pb_box.options[elements.charisma_from_pb_box.selectedIndex].value;
}

// Functions that are called from the HTML ------------------------------------------------------------------------
// All of these just call other functions. Do not change any of their names because they're referenced in views.py.

function onCharClassChange(){
    console.log("You just changed your class");
}

function onRaceChange(){
    console.log("You just changed your race");
}

function onAbilityScoreChange(){
    console.log("You just changed an ability score");
}

function onSubclassChange(){
    console.log("You just changed your subclass");
}

function onBackgroundChange(){
    console.log("You just changed your background");
}


// Helper functions to get something from something else ----------------------------------------------------------

function getDescriptionFromName(name_arg){
    //Given a class, (sub)race, subclass, or specialization, this function returns its description.
    //It is returned as raw html in quotes. The quotes are important because when its output is set
    //as the innerHTML of an element, JS knows that it's supposed to be a string.
    
    var name = name_arg;
    var description;

    //This replaces spaces or dashes in the incoming name with \s or \-, respectively
    name = name.replace(/\s/g,"\\s");
    name = name.replace(/\-/g,"\\-");

    //This returns the name and its description, up to but not including the first instance of the literals '}
    re1 = new RegExp("u\\'((?:" + name + ").*?(?=\\'\\}))");

    description = re1.exec(DATA)[0]

    //This trims it to get strictly the HTML for the description.
    re2 = new RegExp( "(?:u\\'.*?u\\')(.*)" );

    d = re2.exec(description);

    return d[1];
}

function getCostFromAbility(ability) {
    //returns the point-buy cost for an ability.

    var cost_table = new Array();
    cost_table [8] = 0;
    cost_table [9] = 1;
    cost_table [10] = 2;
    cost_table [11] = 3;
    cost_table [12] = 4;
    cost_table [13] = 5;
    cost_table [14] = 7;
    cost_table [15] = 9;
    cost_table [16] = 12;
    cost_table [17] = 15;
    cost_table [18] = 19;

    return cost_table[ability]        
}

function getModifierFromAbility(ability) {
    //returns the modifier (-1 to +4) on an ability score.

    var to_return =  Math.floor( 0.5 * (ability - 10) );
    if (to_return >= 0 ){
        return "+" + to_return.toString();
    } else {
        return to_return.toString();
    }
}

function getSubclassesFromClass(char_class){

    var to_return = [];

    switch (char_class) {
        case "Bard":
            to_return = ["College of Lore", "College of Valor"];
            break;
        case "Barbarian":
            to_return = ["Path of the Berserker", "Path of the Totem Warrior"];
            break;
        case "Cleric":
            to_return = ["Knowledge Domain", "Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain"];
            break;
        case "Druid":
            to_return = ["Circle of the Land", "Circle of the Moon"];
            break;
        case "Fighter":
            to_return = ["Champion", "Battle Master", "Eldritch Knight"]
            break;
        case "Monk":
            to_return = ["Way of the Open Hand", "Way of the Shadow", "Way of the Four Elements"];
            break;
        case "Paladin":
            to_return = ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"];
            break;
        case "Ranger":
            to_return = ["Hunter", "Beast Master"];
            break;
        case "Rogue":
            to_return = ["Thief", "Assassin", "Arcane Trickster"];
            break;
        case "Sorcerer":
            to_return = ["Draconic Bloodline", "Wild Magic"];
            break;
        case "Warlock":
            to_return = ["The Archfey", "The Fiend", "The Great Old One"];
            break;
        case "Wizard":
            to_return = ["School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Illusion", "School of Necromancy", "School of Transmutation"];
            break;
        case "---------":
            to_return = [];
            break;
    }

    return to_return;
}

function getModifiersFromRace(race){

}

//Functions that actually do things on the page -------------------------------------------------------------------

function calculateTotalPoints(){

}

function setAbilityScoreTotals(){

}

function setRaceDescription(){

}

function setClassDescription(){
    
}

function setSubclassDescription(){
    
}

function setBackgroundDescription(){
    
}




/*
function setTotalAbilityScores(){
    //Sets the values of each total ability score and modifier.

    elements.strength_total_box.innerHTML = 
    (parseInt( elements.strength_from_pb ) + parseInt( elements.strength_from_race ) ).toString();
        elements.dexterity_total_box.innerHTML = (
            parseInt( elements.dexterity_from_pb )   +  parseInt(elements . dexterity_from_race)).toString();
        elements.constitution_total_box.innerHTML = (
            parseInt( elements.constitution_from_pb )   +  parseInt(elements . constitution_from_race)).toString();
        elements.intelligence_total_box.innerHTML = (
            parseInt( elements.intelligence_from_pb )   +  parseInt(elements . intelligence_from_race)).toString();
        elements.wisdom_total_box.innerHTML = (
            parseInt( elements.wisdom_from_pb )   +  parseInt(elements . wisdom_from_race)).toString();
        elements.charisma_total_box.innerHTML = (
            parseInt( elements.charisma_from_pb )   +  parseInt(elements . charisma_from_race)).toString();

    strength_mod_box.innerHTML = 
    getModifierFromAbility( parseInt( elements.strength_from_pb ) + parseInt( elements.strength_from_race ) );
        dexterity_mod_box.innerHTML = getModifierFromAbility(parseInt(elements.dexterity_from_pb) + parseInt(elements.dexterity_from_race));
        constitution_mod_box.innerHTML = getModifierFromAbility(parseInt(elements.constitution_from_pb) + parseInt(elements.constitution_from_race));
        intelligence_mod_box.innerHTML = getModifierFromAbility(parseInt(elements.intelligence_from_pb) + parseInt(elements.intelligence_from_race));
        wisdom_mod_box.innerHTML = getModifierFromAbility(parseInt(elements.wisdom_from_pb) + parseInt(elements.wisdom_from_race));
        charisma_mod_box.innerHTML = getModifierFromAbility(parseInt(elements.charisma_from_pb) + parseInt(elements.charisma_from_race));
}

function updateAbiiltyScores() {
    //Calculates how many point-buy points the user has spent on their ability scores.

    var strength_box = document.getElementById("id_strength");
        var dexterity_box = document.getElementById("id_dexterity");
        var constitution_box = document.getElementById("id_constitution");
        var intelligence_box = document.getElementById("id_intelligence");
        var wisdom_box = document.getElementById("id_wisdom");
        var charisma_box = document.getElementById("id_charisma");

    var strength = strength_box.options[strength_box.selectedIndex].value;
        var dexterity = dexterity_box.options[dexterity_box.selectedIndex].value;
        var constitution = constitution_box.options[constitution_box.selectedIndex].value;
        var intelligence = intelligence_box.options[intelligence_box.selectedIndex].value;
        var wisdom = wisdom_box.options[wisdom_box.selectedIndex].value;
        var charisma = charisma_box.options[charisma_box.selectedIndex].value;

    var total_cost = getCost(strength) + getCost(dexterity) + getCost(constitution) + getCost(intelligence) + getCost(wisdom) + getCost(charisma);

    document.getElementById("total_ability_score_box").innerHTML = total_cost.toString();

    getTotalAbilityScores();
}

function updateRaceMods(race){
    // Displays the racial modifiers to ability scores.

    var race_box = document.getElementById("id_race");
    var race = race_box.options[race_box.selectedIndex].text;

    var strength_box = document.getElementById("race_mod_strength");
        var dexterity_box = document.getElementById("race_mod_dexterity");
        var constitution_box = document.getElementById("race_mod_constitution");
        var intelligence_box = document.getElementById("race_mod_intelligence");
        var wisdom_box = document.getElementById("race_mod_wisdom");
        var charisma_box = document.getElementById("race_mod_charisma");

    var race_mods = [];


    switch (race) {  
        case "Human":
            race_mods["strength"] = "+1";
            race_mods["dexterity"] = "+1";
            race_mods["constitution"] = "+1";
            race_mods["intelligence"] = "+1";
            race_mods["wisdom"] = "+1";
            race_mods["charisma"] = "+1";
            break;
        case "Tiefling":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+1";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+2";
            break;
        case "Half-Orc":
            race_mods["strength"] = "+2";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+1";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
            break;
        case "Half-Elf":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+2";
            break;
        case "Gnome - Forest":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+1";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+2";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
            break;
        case "Gnome - Rock":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+1";
            race_mods["intelligence"] = "+2";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
            break;
        case "Dragonborn":
            race_mods["strength"] = "+2";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+1";
            break;
        case "Halfling - Stout":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+2";
            race_mods["constitution"] = "+1";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
            break;
        case "Halfling - Lightfoot":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+2";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+1";
            break;
        case "Elf - Dark (Drow)":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+2";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+1";
            break;
        case "Elf - Wood":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+2";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+1";
            race_mods["charisma"] = "+0";
            break;
        case "Elf - High":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+2";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+1";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
            break;
        case "Dwarf - Mountain":
            race_mods["strength"] = "+2";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+2";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
            break;
        case "Dwarf - Hill":
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+1";
            race_mods["charisma"] = "+2";
            break;
        default:
            race_mods["strength"] = "+0";
            race_mods["dexterity"] = "+0";
            race_mods["constitution"] = "+0";
            race_mods["intelligence"] = "+0";
            race_mods["wisdom"] = "+0";
            race_mods["charisma"] = "+0";
    } 

    strength_box.innerHTML = race_mods["strength"];
        dexterity_box.innerHTML = race_mods["dexterity"];
        constitution_box.innerHTML = race_mods["constitution"];
        intelligence_box.innerHTML = race_mods["intelligence"];
        wisdom_box.innerHTML = race_mods["wisdom"];
        charisma_box.innerHTML = race_mods["charisma"]; 

    getTotalAbilityScores();
}

function updateRaceDescription() {
    //Updates the descriptions for the currently selected race and subrace.

    var race_box = document.getElementById("id_race");
    var race = race_box.options[race_box.selectedIndex].text;
    var race_description_box = document.getElementById("race_explanation")
    var subrace_description_box = document.getElementById("subrace_explanation")

    switch (race) {  
        case "Human":
            race_description_box.innerHTML = "<b>Humans</b> are the most varied race. They are ambitious, but short-lived.";    
            subrace_description_box.innerHTML = "Humans have widely varying ethnicities, unlike other races.";
            break;
        case "Tiefling":
            race_description_box.innerHTML = "<b>Tieflings</b> are humanoids related to evil outsiders: the devils or demons.";    
            subrace_description_box.innerHTML = "Even the weakest of tieflings can cast some spells.";
            break;
        case "Half-Orc":
            race_description_box.innerHTML = "<b>Half-orcs</b> are often stereotyped as monsters, but they're not always villains.";    
            subrace_description_box.innerHTML = "Half-orcs are strong and tough, and they can see in the dark.";
            break;
        case "Half-Elf":
            race_description_box.innerHTML = "<b>Half-elves</b> are born to human and elven parents, and they have some characteristics of both. ";    
            subrace_description_box.innerHTML = "They can blend in with humans or elves, but are neither.";
            break;
        case "Gnome - Forest":
            race_description_box.innerHTML = "<b>Gnomes</b> are tiny and impulsive. They're bold or foolhardy, depending who you ask.";    
            subrace_description_box.innerHTML = "<b>Forest Gnomes</b> have a knack for illusions and stealth.";
            break;
        case "Gnome - Rock":
            race_description_box.innerHTML = "<b>Gnomes</b> are tiny and impulsive. They're bold or foolhardy, depending who you ask.";    
            subrace_description_box.innerHTML = "<b>Rock Gnomes</b> are commonly tinkerers, inventors, and alchemists.";
            break;
        case "Dragonborn":
            race_description_box.innerHTML = "<b>Dragonborn</b> are strong, charismatic humanoids hatched from dragon eggs. ";    
            subrace_description_box.innerHTML = "Dragonborn can breathe fire, lightning, ice, or another element.";
            break;
        case "Halfling - Stout":
            race_description_box.innerHTML = "<b>Halflings</b>, also called <b>hobbits</b>, enjoy the finer things in life: food, drink, and friends.";    
            subrace_description_box.innerHTML = "<b>Stout Halflings</b> are hardier than average and are soemtimes related to dwarves.";
            break;
        case "Halfling - Lightfoot":
            race_description_box.innerHTML = "<b>Halflings</b>, also called <b>hobbits</b>, enjoy the finer things in life: food, drink, and friends.";    
            subrace_description_box.innerHTML = "<b>Lightfoot halflings</b> are even smaller and more prone to wanderlust.";
            break;
        case "Elf - Dark (Drow)":
            race_description_box.innerHTML = "<b>Elves</b> are slender and graceful, and live for centuries. They love art, nature, and magic.";    
            subrace_description_box.innerHTML = "<b>Dark elves</b> were banished from the surface world. They now live underground.";
            break;
        case "Elf - Wood":
            race_description_box.innerHTML = "<b>Elves</b> are slender and graceful, and live for centuries. They love art, nature, and magic.";    
            subrace_description_box.innerHTML = "<b>Wood elves</b> have keen senses and intuition, and they live in forests.";
            break;
        case "Elf - High":
            race_description_box.innerHTML = "<b>Elves</b> are slender and graceful, and live for centuries. They love art, nature, and magic.";    
            subrace_description_box.innerHTML = "<b>High elves</b> are extremely intelligent. All of them have at least some magic.";
            break;
        case "Dwarf - Mountain":
            race_description_box.innerHTML = "<b>Dwarves</b> are short and stout. They love mining and smithing, and they value their clans.";    
            subrace_description_box.innerHTML = "<b>Mountain dwarves</b> live in difficult terrain, and as such are especially strong.";
            break;
        case "Dwarf - Hill":
            race_description_box.innerHTML = "<b>Dwarves</b> are short and stout. They love mining and smithing, and they value their clans.";    
            subrace_description_box.innerHTML = "<b>Hill dwarves</b> have keen senses, and are connected to the earth around them.";
            break;
    }

    updateRaceMods();
}

function updateClassDescription(){
    //Updates the description for the currently selected class.

    var class_box = document.getElementById("id_character_class");
    var char_class = class_box.options[class_box.selectedIndex].text;
    var class_description_box = document.getElementById("class_explanation");

    switch (char_class) {
        case "Barbarian":
            class_description_box.innerHTML = "<b>Barbarians</b> are fierce warriors from a primitive background who can enter a rage.";    
            break;
        case "Bard":
            class_description_box.innerHTML = "<b>Bards</b> are magicians who can inspire their allies with songs.";    
            break;
        case "Cleric":
            class_description_box.innerHTML = "<b>Clerics</b> are priestly champions who use divine magic in service of a higher power.";    
            break;
        case "Druid":
            class_description_box.innerHTML = "<b>Druids</b> are priests of nature who can transform into animals and cast spells.";    
            break;
        case "Fighter":
            class_description_box.innerHTML = "<b>Fighters</b> are masters of martial combat. They are masters of weapons and armor.";    
            break;
        case "Paladin":
            class_description_box.innerHTML = "<b>Paladins</b> are holy warriors bound to a sacred oath. They use weapons and holy magic.";    
            break;
        case "Monk":
            class_description_box.innerHTML = "<b>Monks</b> are masters of martial arts. They pursue physical and spiritual perfection.";    
            break;
        case "Ranger":
            class_description_box.innerHTML = "<b>Rangers</b> are hunters who use martial prowess and nature magic.";    
            break;
        case "Rogue":
            class_description_box.innerHTML = "<b>Rogues</b> are scoundrels who use stealth and trickery to overcome problems.";    
            break;
        case "Sorcerer":
            class_description_box.innerHTML = "<b>Sorcerers</b> are spellcasters who get their power from their magical ancestry.";    
            break;
        case "Warlock":
            class_description_box.innerHTML = "<b>Warlocks</b> are spellcasters who made a pact with a poweful being for their power.";    
            break;
        case "Wizard":
            class_description_box.innerHTML = "<b>Wizards</b> are spellcasters who earn their power through rigorous study.";
            break;        
    }

    updateSubclass();
}

function updateBackgroundDescription(){
    var background_box = document.getElementById("id_background");
    var background = background_box.options[background_box.selectedIndex].text;
    var background_description_box = document.getElementById("background_explanation");
    switch (background) {
        case "Acolyte":
            background_description_box.innerHTML = "<b>Acolytes</b> spent their lives in the service of a temple to a specific god or pantheon of gods.";
            break;
        case "Charlatan":
            background_description_box.innerHTML = "<b>Charlatans</b> have always had a way with people - and are perfectly willing to use this to their advantage.";
            break;
        case "Criminal":
            background_description_box.innerHTML = "<b>Criminals</b> have a history of breaking the law and have contacts within the criminal underworld.";
            break;
        case "Entertainer":
            background_description_box.innerHTML = "<b>Entertainers</b> thrive in front of an audience, and know how to entrance, entertain, and even inspire them.";
            break;
        case "Folk Hero":
            background_description_box.innerHTML = "<b>Folk Heroes</b> come from humble social ranks, but are already regarded by their home villages as champions.";
            break;
        case "Guild Artisan":
            background_description_box.innerHTML = "<b>Guild Artisans</b> are members of a guild, skilled in a particular field and associated with other artisans.";
            break;
        case "Hermit":
            background_description_box.innerHTML = "<b>Hermits</b> lived in seclusion for a formative part of their lives.";
            break;
        case "Noble":
            background_description_box.innerHTML = "<b>Nobles</b> carry a noble title and understand wealth, power, and privilege.";
            break;
        case "Outlander":
            background_description_box.innerHTML = "<b>Outlanders</b> grew up in the wilds, far from civilization and the comforts of town and technology.";
            break;
        case "Sage":
            background_description_box.innerHTML = "<b>Sages</b> spent years learning the lore of the multiverse, making them masters in their fields of study.";
            break;
        case "Sailor":
            background_description_box.innerHTML = "<b>Sailors</b> sailed on seagoing vessels for years.";
            break;
        case "Soldier":
            background_description_box.innerHTML = "<b>Soldiers</b> have trained and fought in wars for most of their lives.";
            break;
        case "Urchin":
            background_description_box.innerHTML = "<b>Urchins</b> grew up on the streets alone, orphaned, and poor, learning to provide for themselves.";
            break;
            }
}



function updateSubclass(){
    var subclass_box = document.getElementById("id_subclass");
    var class_box = document.getElementById("id_character_class");
    var char_class = class_box.options[class_box.selectedIndex].text;

    //delete all options in the subclass box
    while ( subclass_box.length > 1) {
        subclass_box.remove(1);
    }

    var subclasses = getSubclassesFromClass(char_class);

    // console.log("Subclasses: ");
    // console.log(subclasses);

    //create new ones corresponding to the appropriate subclass
    for (var i = 1; i <= subclasses.length; i++) {
        var new_option = document.createElement('option');
        new_option.value = i;
        new_option.innerHTML = subclasses[i-1];
        subclass_box.appendChild(new_option);
        // console.log("Creating new option: ");
        // console.log(new_option)
    }
    
    updateSubclassDescription()
}

function updateSubclassDescription()
{
    var subclass_box = document.getElementById("id_subclass");
    var subclass = subclass_box.options[subclass_box.selectedIndex].text;
    var subclass_description_box = document.getElementById("subclass_explanation");
    
    switch (subclass) {
        case "College of Lore":
            subclass_description_box.innerHTML = "Bards in the <b>College of Lore</b> pursue beauty and truth, collecting knowledge from sources as diverse as scholarly tomes and peasant tales.";
            break;
        case "College of Valor":
            subclass_description_box.innerHTML = "Bards of the <b>College of Valor</b> are daring skalds whose tales keep alive the memory of the great heroes of the past.";
            break;
        case "Path of the Berserker":
            subclass_description_box.innerHTML = "Barbarians who follow the <b>Path of the Berserker</b> thrill in the chaos of battle and delight in violence and their untrammeled fury.";
            break;
        case "Path of the Totem Warrior":
            subclass_description_box.innerHTML = "Barbarians who follow the <b>Path of the Totem Warrior</b> choose a spirit animal to guide, protect, and inspire them in battle.";
            break;
        case "Knowledge Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>Knowledge Domain</b> study esoteric lore, collect old tomes, delve into the secret places of earth, and learn all they can.";
            break;
        case "Life Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>Life Domain</b> focus on the vibrant positive energy that sustains all live, healing the sick and wounded, caring for those in need, and driving away the forces of death and undeath.";
            break;
        case "Light Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>Light Domain</b> are enlightened souls infused with radiance and the power of their gods' discerning vision, charged with chasing away lies and burning away darkness.";
            break;
        case "Nature Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>Nature Domain</b> might hunt the evil monstrosities that despoil the woodlands, bless the harvest of the faithful, or wither the crops of those who anger their gods.";
            break;
        case "Tempest Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>Tempest Domain</b> seek to inspire fear in the common folk, either to keep those folk on the path of righteousness or to encourage them to offer sacrifices of propitiation to ward off divine wrath.";
            break;
        case "Trickery Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>Trickery Domain</b> are a disruptive force in the world, prefering subterfuge, pranks, deception, and theft rather than direct confrontation.";
            break;
        case "War Domain":
            subclass_description_box.innerHTML = "Clerics who emphasize the <b>War Domain</b> excel in battle, inspiring others to fight the good fight or offering acts of violence as prayers.";
            break;
        case "Circle of the Land":
            subclass_description_box.innerHTML = "Druid members of the <b>Circle of Land</b> have magic influenced by the land where they were initiated into the circle's mysterious rites.";
            break;
        case "Circle of the Moon":
            subclass_description_box.innerHTML = "Druid members of the <b>Circle of the Moon</b> haunt the deepest parts of the wild and are as changeable as the moon.";
            break;
        case "Champion":
            subclass_description_box.innerHTML = "Fighters who emulate the <b>Champion</b> archetype focus on developing raw physical power honed to deadly perfection.";
            break;
        case "Battle Master":
            subclass_description_box.innerHTML = "Fighters who emulate the <b>Battle Master</b> archetype employ martial techniques passed down through generations and treat combat as an academic field.";
            break;
        case "Eldritch Knight":
            subclass_description_box.innerHTML = "Fighters who emulate the <b>Eldritch Knight</b> archetype combine martial mastery with a careful study of magic.";
            break;
        case "Way of the Open Hand":
            subclass_description_box.innerHTML = "Monks of the <b>Way of the Open Hand</b> are the ultimate masters of martial arts combat, whether armed or unarmed.";
            break;
        case "Way of the Shadow":
            subclass_description_box.innerHTML = "Monks of the <b>Way of the Shadow</b> value stealth and subterfuge, and might serve as spies or assassins.";
            break;
        case "Way of the Four Elements":
            subclass_description_box.innerHTML = "Monks of the <b>Way of the Four Elements</b> align themselves with the forces of creation and bend the four elements to their will.";
            break;
        case "Oath of Devotion":
            subclass_description_box.innerHTML = "Paladins sworn to the <b>Oath of Devotion</b> are bound to the loftiest ideals of justice, virtue, and order, holding themselves and sometimes the world to the highest standards of conduct.";
            break;
        case "Oath of the Ancients":
            subclass_description_box.innerHTML = "Paladins sworn to the <b>Oath of the Ancients</b> cast their lot with the side of the light int he cosmic struggle against darkness because they love the beautiful and life-giving things of the world.";
            break;
        case "Oath of Vengeance":
            subclass_description_box.innerHTML = "Paladins sworn to the <b>Oath of Vengeance</b> are devoted to punishing those who have committed a grievous sin and hold delivering justice above their own purity.";
            break;
        case "Hunter":
            subclass_description_box.innerHTML = "Rangers who emulate the <b>Hunter</b> archetype accept their place as a bulwark between civilization and the terrors of the wilderness.";
            break;
        case "Beast Master":
            subclass_description_box.innerHTML = "Rangers who emulate the <b>Beast Master</b> archetype embody a friendship between the civilized races and the beasts of the world, working in partnership with an animal.";
            break;
        case "Thief":
            subclass_description_box.innerHTML = "Rogues who prefer the techniques of the <b>Thief</b> hone their skills in the larcenous arts, and are often burglars, bandits, treasure seekers, or explorers.";
            break;
        case "Assassin":
            subclass_description_box.innerHTML = "Rogues who prefer the techniques of the <b>Assassin</b> focus their training on the grim art of death, using stealth, poison, and disguise to eliminate foes with deadly efficiency.";
            break;
        case "Arcane Trickster":
            subclass_description_box.innerHTML = "Rogues who prefer the techniques of the <b>Arcane Trickster</b> enhance their fine-honed skills of stealth and agility with magic, learning tricks of enchantment and illusion.";
            break;
        case "Draconic Bloodline":
            subclass_description_box.innerHTML = "Sorcerers with the <b>Draconic Bloodline</b> origin trace their descent back to a mighty sorcerer who made a bargain with a dragon or claimed a dragon parent.";
            break;
        case "Wild Magic":
            subclass_description_box.innerHTML = "Sorcerers with the <b>Wild Magic</b> origin get their magic from the wild forces of chaos that underlie the order of creation.";
            break;
        case "The Archfey":
            subclass_description_box.innerHTML = "Warlocks of <b>The Archfey</b> have a lord or lady of the fey patron with inscrutable and sometimes whimsical motivations.";
            break;
        case "The Fiend":
            subclass_description_box.innerHTML = "Warlocks of <b>The Fiend</b> made a pact with a fiend from the lower planes of existence, a being whose aims are evil and desire total corruption or destruction of all things.";
            break;
        case "The Great Old One":
            subclass_description_box.innerHTML = "Warlocks of <b>The Great Old One</b> have a mysterious entity of an utterly foreign nature for a patron with motives incomprehensible to mortals, and may be unaware of or indifferent to your existance.";
            break;
        case "School of Abjuration":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Abjuration</b> emphasize magic that blocks, banishes, or protects.";
            break;
        case "School of Conjuration":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Conjuration</b> favor spells that produce objects and creatures out of thin air.";
            break;
        case "School of Divination":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Divination</b> strive to part the veils of space, time, and consciousness so that they can see clearly.";
            break;
        case "School of Enchantment":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Enchantment</b> have honed their ability to magically entrance and beguile other people and monsters.";
            break;
        case "School of Evocation":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Evocation</b> focus on magic that creates powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid.";
            break;
        case "School of Illusion":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Illusion</b> focus on magic that dazzles the senses, befuddles the mind, and tricks even the wisest folk.";
            break;
        case "School of Necromancy":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Necromancy</b> explore the cosmic forces of life, death, and undeath.";
            break;
        case "School of Transmutation":
            subclass_description_box.innerHTML = "Wizards of the <b>School of Transmutation</b> study spells that modify energy and matter.";
            break;
        default:
            subclass_description_box.innerHTML = "Members of this subclass are...";
    }
}


updateSubclass(); 
*/

