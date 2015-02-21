document.title = "D&D 5E Character Generator"
var elements;
window.onload = function(){
    console.log ("window ready");

            //This object contains variable names for all the useful elements on the page.
        elements = {
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

            strength_race_box : document.getElementById("race_mod_strength"),
                dexterity_race_box : document.getElementById("race_mod_dexterity"),
                constitution_race_box : document.getElementById("race_mod_constitution"),
                intelligence_race_box : document.getElementById("race_mod_intelligence"),
                wisdom_race_box : document.getElementById("race_mod_wisdom"),
                charisma_race_box : document.getElementById("race_mod_charisma"),
        };

        updateElements();
        updateSubclass();
    }

// Functions that are called from the HTML ------------------------------------------------------------------------
// All of these just call other functions. Do not change any of their names because they're referenced in views.py.

function onCharClassChange(){
    setClassDescription();
    updateSubclass();
    console.log("You just changed your class");
}

function onRaceChange(){
    setRaceDescription();
    setRaceModifiers();
    console.log("You just changed your race");
}

function onAbilityScoreChange(){
    updateElements();
    calculateTotalPoints();
    setAbilityScoreTotals();
    setAbilityModifiers();
    console.log("You just changed an ability score");
}

function onSubclassChange(){
    setSubclassDescription();
    console.log("You just changed your subclass");
}

function onBackgroundChange(){
    setBackgroundDescription();
    console.log("You just changed your background");
}


// Helper functions to get something from something else ----------------------------------------------------------

function getDescriptionFromName(name_arg){
    //Given a class, (sub)race, subclass, or specialization, this function returns its description.
    //It is returned as raw html in quotes. The quotes are important because when its output is set
    //as the innerHTML of an element, JS knows that it's supposed to be a string.
    
    var name = name_arg;
    if (name =="---------") {
        return "dMembers of this subclass are...d";
    }
    var description;

    //This replaces spaces or dashes in the incoming name with \s or \-, respectively
    name = name.replace(/\s/g,"\\s");
    name = name.replace(/\-/g,"\\-");
    name = name.replace(/\(/g,"\\(");
    name = name.replace(/\)/g,"\\)");

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
    
    setSubclassDescription()
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

function getModifiersFromRace(race,ability){
    var name = race;
    if (name =="---------") {
        return "+0";
    }
    var description;

    //This replaces spaces or dashes in the incoming name with \s or \-, respectively
    name = name.replace(/\s/g,"\\s");
    name = name.replace(/\-/g,"\\-");
    name = name.replace(/\(/g,"\\(");
    name = name.replace(/\)/g,"\\)");

    //This returns the name and its description, up to but not including the first instance of the literals '}
    re1 = new RegExp("u\\'((?:" + name + ").*?(?=\\}))");

    description = re1.exec(MOD_DATA)[0]

    //This trims it to get strictly the HTML for the description.
    re2 = new RegExp( "(?:\\[.*?\\])(.*)" );

    d = re2.exec(description);

    var to_return;
    if (ability=="strength") {
        to_return = d[0].substring(1,2);
    }
    else if (ability=="dexterity") {
        to_return = d[0].substring(4,5);
    }
    else if (ability=="constitution") {
        to_return = d[0].substring(7,8);
    }
    else if (ability=="intelligence") {
        to_return = d[0].substring(10,11);
    }
    else if (ability=="wisdom") {
        to_return = d[0].substring(13,14);
    }
    else if (ability=="charisma") {
        to_return = d[0].substring(16,17);
    }
    console.log(to_return);
    if (parseInt(to_return) >= 0 ){
        return "+" + to_return;
    } else {
        return to_return;
    }
}

//Functions that actually do things on the page -------------------------------------------------------------------

function updateElements(){
    elements.strength_from_pb = elements.strength_from_pb_box.options[elements.strength_from_pb_box.selectedIndex].value;
    elements.dexterity_from_pb = elements.dexterity_from_pb_box.options[elements.dexterity_from_pb_box.selectedIndex].value;
    elements.constitution_from_pb = elements.constitution_from_pb_box.options[elements.constitution_from_pb_box.selectedIndex].value;
    elements.intelligence_from_pb = elements.intelligence_from_pb_box.options[elements.intelligence_from_pb_box.selectedIndex].value;
    elements.wisdom_from_pb = elements.wisdom_from_pb_box.options[elements.wisdom_from_pb_box.selectedIndex].value;
    elements.charisma_from_pb = elements.charisma_from_pb_box.options[elements.charisma_from_pb_box.selectedIndex].value;
}

function calculateTotalPoints(){
    var strength = getCostFromAbility(parseInt( elements.strength_from_pb ));
    var dexterity = getCostFromAbility(parseInt( elements.dexterity_from_pb ));
    var constitution = getCostFromAbility(parseInt( elements.constitution_from_pb ));
    var intelligence = getCostFromAbility(parseInt( elements.intelligence_from_pb ));
    var wisdom = getCostFromAbility(parseInt( elements.wisdom_from_pb ));
    var charisma = getCostFromAbility(parseInt( elements.charisma_from_pb ));
    var total_cost = dexterity+strength+constitution+intelligence+wisdom+charisma;
    document.getElementById("total_ability_score_box").innerHTML = total_cost.toString();
}

function setAbilityScoreTotals(){
    var strength = parseInt( elements.strength_from_pb ) + parseInt(elements.strength_race_box.innerHTML);
    var dexterity = parseInt( elements.dexterity_from_pb ) + parseInt(elements.dexterity_race_box.innerHTML);
    var constitution = parseInt( elements.constitution_from_pb ) + parseInt(elements.constitution_race_box.innerHTML);
    var intelligence = parseInt( elements.intelligence_from_pb ) + parseInt(elements.intelligence_race_box.innerHTML);
    var wisdom = parseInt( elements.wisdom_from_pb ) + parseInt(elements.wisdom_race_box.innerHTML);
    var charisma = parseInt( elements.charisma_from_pb ) + parseInt(elements.charisma_race_box.innerHTML);
    document.getElementById("total_strength_score").innerHTML = strength.toString();
    document.getElementById("total_dexterity_score").innerHTML = dexterity.toString();
    document.getElementById("total_constitution_score").innerHTML = constitution.toString();
    document.getElementById("total_intelligence_score").innerHTML = intelligence.toString();
    document.getElementById("total_wisdom_score").innerHTML = wisdom.toString();
    document.getElementById("total_charisma_score").innerHTML = charisma.toString();
    setAbilityModifiers();
}

function setAbilityModifiers(){
    var strength = getModifierFromAbility(parseInt(document.getElementById("total_strength_score").innerHTML))
    var dexterity = getModifierFromAbility(parseInt(document.getElementById("total_dexterity_score").innerHTML))
    var constitution = getModifierFromAbility(parseInt(document.getElementById("total_constitution_score").innerHTML))
    var intelligence = getModifierFromAbility(parseInt(document.getElementById("total_intelligence_score").innerHTML))
    var wisdom = getModifierFromAbility(parseInt(document.getElementById("total_wisdom_score").innerHTML))
    var charisma = getModifierFromAbility(parseInt(document.getElementById("total_charisma_score").innerHTML))
    document.getElementById("total_strength_mod").innerHTML = strength;
    document.getElementById("total_dexterity_mod").innerHTML = dexterity;
    document.getElementById("total_constitution_mod").innerHTML = constitution;
    document.getElementById("total_intelligence_mod").innerHTML = intelligence;
    document.getElementById("total_wisdom_mod").innerHTML = wisdom;
    document.getElementById("total_charisma_mod").innerHTML = charisma;
}

function setRaceModifiers(){
    var race_box = document.getElementById("id_race");
    var race = race_box.options[race_box.selectedIndex].text;
    elements.strength_race_box.innerHTML = getModifiersFromRace(race,"strength");
    elements.dexterity_race_box.innerHTML = getModifiersFromRace(race,"dexterity");
    elements.constitution_race_box.innerHTML = getModifiersFromRace(race,"constitution");
    elements.intelligence_race_box.innerHTML = getModifiersFromRace(race,"intelligence");
    elements.wisdom_race_box.innerHTML = getModifiersFromRace(race,"wisdom");
    elements.charisma_race_box.innerHTML = getModifiersFromRace(race,"charisma");
    setAbilityScoreTotals();
}

function setRaceDescription(){
    var race_box = document.getElementById("id_race");
    var race = race_box.options[race_box.selectedIndex].text;
    var race_description_box = document.getElementById("race_explanation");
    var stringDesc = getDescriptionFromName(race);
    race_description_box.innerHTML = stringDesc.substring(1,stringDesc.length-1);
}

function setClassDescription(){
    var class_box = document.getElementById("id_character_class");
    var class2 = class_box.options[class_box.selectedIndex].text;
    var class_description_box = document.getElementById( "class_explanation");
    var stringDesc = getDescriptionFromName(class2);
    class_description_box.innerHTML = stringDesc.substring(1,stringDesc.length-1);
    
}

function setSubclassDescription(){
    var subclass_box = document.getElementById("id_subclass");
    var subclass = subclass_box.options[subclass_box.selectedIndex].text;
    var subclass_description_box = document.getElementById("subclass_explanation");
    var stringDesc = getDescriptionFromName(subclass);
    subclass_description_box.innerHTML = stringDesc.substring(1,stringDesc.length-1);
}

function setBackgroundDescription(){
    var background_box = document.getElementById("id_background");
    var background = background_box.options[background_box.selectedIndex].text;
    var background_description_box = document.getElementById("background_explanation");
    var stringDesc = getDescriptionFromName(background);
    background_description_box.innerHTML = stringDesc.substring(1,stringDesc.length-1);
}