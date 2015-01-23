//I would wrap all of these functions in a class for this page to avoid cluttering the global scope,
//but given that this is the only javascript that will be used I don't think that will be an issue.

function getTotalAbilityScores(){
    //Sets the values of each total ability score and modifier.

    //These sets of six are indented so you can collapse them.
    var strength_total_box = document.getElementById("total_strength_score");
        var dexterity_total_box = document.getElementById("total_dexterity_score");
        var constitution_total_box = document.getElementById("total_constitution_score");
        var intelligence_total_box = document.getElementById("total_intelligence_score");
        var wisdom_total_box = document.getElementById("total_wisdom_score");
        var charisma_total_box = document.getElementById("total_charisma_score");

    var strength_mod_box = document.getElementById("total_strength_mod");
        var dexterity_mod_box = document.getElementById("total_dexterity_mod");
        var constitution_mod_box = document.getElementById("total_constitution_mod");
        var intelligence_mod_box = document.getElementById("total_intelligence_mod");
        var wisdom_mod_box = document.getElementById("total_wisdom_mod");
        var charisma_mod_box = document.getElementById("total_charisma_mod");

    var strength_from_pb_box = document.getElementById("id_ab_score_form-strength");
        var dexterity_from_pb_box = document.getElementById("id_ab_score_form-dexterity");
        var constitution_from_pb_box = document.getElementById("id_ab_score_form-constitution");
        var intelligence_from_pb_box = document.getElementById("id_ab_score_form-intelligence");
        var wisdom_from_pb_box = document.getElementById("id_ab_score_form-wisdom");
        var charisma_from_pb_box = document.getElementById("id_ab_score_form-charisma");

    var strength_from_pb = strength_from_pb_box.options[strength_from_pb_box.selectedIndex].value;
        var dexterity_from_pb = dexterity_from_pb_box.options[dexterity_from_pb_box.selectedIndex].value;
        var constitution_from_pb = constitution_from_pb_box.options[constitution_from_pb_box.selectedIndex].value;
        var intelligence_from_pb = intelligence_from_pb_box.options[intelligence_from_pb_box.selectedIndex].value;
        var wisdom_from_pb = wisdom_from_pb_box.options[wisdom_from_pb_box.selectedIndex].value;
        var charisma_from_pb = charisma_from_pb_box.options[charisma_from_pb_box.selectedIndex].value;

    var strength_from_race = document.getElementById("race_mod_strength").innerHTML;
        var dexterity_from_race = document.getElementById("race_mod_dexterity").innerHTML;
        var constitution_from_race = document.getElementById("race_mod_constitution").innerHTML;
        var intelligence_from_race = document.getElementById("race_mod_intelligence").innerHTML;
        var wisdom_from_race = document.getElementById("race_mod_wisdom").innerHTML;
        var charisma_from_race = document.getElementById("race_mod_charisma").innerHTML;

    strength_total_box.innerHTML = (parseInt(strength_from_pb)+parseInt(strength_from_race)).toString();
        dexterity_total_box.innerHTML = (parseInt(dexterity_from_pb) + parseInt(dexterity_from_race)).toString();
        constitution_total_box.innerHTML = (parseInt(constitution_from_pb) + parseInt(constitution_from_race)).toString();
        intelligence_total_box.innerHTML = (parseInt(intelligence_from_pb) + parseInt(intelligence_from_race)).toString();
        wisdom_total_box.innerHTML = (parseInt(wisdom_from_pb) + parseInt(wisdom_from_race)).toString();
        charisma_total_box.innerHTML = (parseInt(charisma_from_pb) + parseInt(charisma_from_race)).toString();

    strength_mod_box.innerHTML=getModifier(parseInt(strength_from_pb)+parseInt(strength_from_race));
        dexterity_mod_box.innerHTML = getModifier(parseInt(dexterity_from_pb) + parseInt(dexterity_from_race));
        constitution_mod_box.innerHTML = getModifier(parseInt(constitution_from_pb) + parseInt(constitution_from_race));
        intelligence_mod_box.innerHTML = getModifier(parseInt(intelligence_from_pb) + parseInt(intelligence_from_race));
        wisdom_mod_box.innerHTML = getModifier(parseInt(wisdom_from_pb) + parseInt(wisdom_from_race));
        charisma_mod_box.innerHTML = getModifier(parseInt(charisma_from_pb) + parseInt(charisma_from_race));
}

function updateAbilityScores() {
    //Calculates how many point-buy points the user has spent on their ability scores.

    var strength_box = document.getElementById("id_ab_score_form-strength");
        var dexterity_box = document.getElementById("id_ab_score_form-dexterity");
        var constitution_box = document.getElementById("id_ab_score_form-constitution");
        var intelligence_box = document.getElementById("id_ab_score_form-intelligence");
        var wisdom_box = document.getElementById("id_ab_score_form-wisdom");
        var charisma_box = document.getElementById("id_ab_score_form-charisma");

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

function getCost(ability) {
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

function getModifier(ability) {
    //returns the modifier (-1 to +4) on an ability score.

    var to_return =  Math.floor( 0.5 * (ability - 10) );
    if (to_return >= 0 ){
        return "+" + to_return.toString();
    } else {
        return to_return.toString();
    }
}

function updateRaceMods(race){
    // Displays the racial modifiers to ability scores.

    var race_box = document.getElementById("id_class_race_form-race");
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
        case "Gnome - Forrest":
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
        case "Elf- High":
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

    var race_box = document.getElementById("id_class_race_form-race");
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
        case "Gnome - Forrest":
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
        case "Elf- High":
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

    var class_box = document.getElementById("id_class_race_form-character_class");
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
            class_description_box.innerHTML = "<b>Wizard</b> are spellcasters who earn their power through rigorous study.";    
            break;        
    }

    updateSubclass();
}

function updateBackgroundDescription(){
    var background_box = document.getElementById("id_background_form-background");
    var background = background_box.options[background_box.selectedIndex].text;
    var background_description_box = document.getElementById("background_explanation");

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
            to_return = ["---------"];
            break;

    }

    return to_return;
}

function updateSubclass(){
    var subclass_box = document.getElementById("id_subclass_form-subclass");
    var class_box = document.getElementById("id_class_race_form-character_class");
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
}


updateSubclass(); 

document.title = "D&D 5E Character Generator"