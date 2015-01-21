"""
This file controls which http responses and html pages are shown.

Functions here should take their input from urls.py and return an 
HttpResponse object.

More information at https://docs.djangoproject.com/en/1.6/intro/tutorial03/
or at https://docs.djangoproject.com/en/1.6/topics/http/views/
"""

"""
    Refactoring idea:
    
    if request.method != 'POST': #if not submitted yet
        return a rendered nameentry template
        pass it no data
        use the entered name to create a new row in the user_entry model with that name
            so that it can track their progress

    elif (the progress parameter indicates they are ready to pick race/class):
        return a rendered classrace template
        pass it data of the character's name to be displayed (not edited)
        use the returned class and race and put them into the user_entry model in the correct row

    elif (the progress parameter indicates they are ready to pick <arbitrary step> ):
        return a rendered <arbitrary step> template
        pass it all data of previus steps so that it can be displayed
        put the returned data into the user_entry model


    Somehow, at the last step, send instructions to another file to write all the stuff to a pdf.

    For some reason, the very presence of this comment causes the next line to throw an indentation error.
    If this comment is removed, it works fine.
"""


import os, sys
sys.path.append('../')
import oursite.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'oursite.settings'
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django import forms
from django.db import models
from django.forms import ModelForm
import pdftest
from character import Character

from models import dChar_class, dRace, user_entry, dbackstory

def pdf_view(request):
    with open('myfile.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'filename=mycharacter.pdf'
        return response
    pdf.closed

class NameInputForm(forms.Form):
    name = forms.CharField()

class ClassRaceForm(forms.Form):
    character_class = forms.ModelChoiceField(
        queryset = dChar_class.objects.all()
    )
    race = forms.ModelChoiceField(
        queryset = dRace.objects.all()
    )
    name = forms.CharField(
        widget = forms.HiddenInput()
    )

class AbilityScoreForm(forms.Form):
    strength     = forms.ChoiceField(
        [
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18)
            ],
        widget = forms.Select(attrs = {
            "onChange": 'updateAbilityScores()'
            })
        )
    dexterity    = forms.ChoiceField(
        [
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18)
        ],
        widget = forms.Select(attrs = {
            "onChange": 'updateAbilityScores()'
            })
        )
    constitution = forms.ChoiceField(
        [
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18)
        ],
        widget = forms.Select(attrs = {
            "onChange": 'updateAbilityScores()'
            })
        )
    intelligence = forms.ChoiceField(
        [
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18)
        ],
        widget = forms.Select(attrs = {
            "onChange": 'updateAbilityScores()'
            })
        )
    wisdom       = forms.ChoiceField(
        [
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18)
        ],
        widget = forms.Select(attrs = {
            "onChange": 'updateAbilityScores()'
            })
        )
    charisma     = forms.ChoiceField(
        [
            (8, 8),
            (9, 9),
            (10, 10),
            (11, 11),
            (12, 12),
            (13, 13),
            (14, 14),
            (15, 15),
            (16, 16),
            (17, 17),
            (18, 18)
        ],
        widget = forms.Select(attrs = {
            "onChange": 'updateAbilityScores()'
            })
        )
    name = forms.CharField(
        widget = forms.HiddenInput()
    )

class BackgroundForm(forms.Form):
    background = forms.ModelChoiceField(
        queryset = dbackstory.objects.all()
    )
    name = forms.CharField(
        widget = forms.HiddenInput()
    )



def index(request):
    index = loader.get_template('chargen/index.html')

    nameentry = loader.get_template('chargen/nameentry.html')
    classrace = loader.get_template('chargen/classrace.html')
    abilityscores = loader.get_template('chargen/abilityscores.html')
    background = loader.get_template('chargen/background.html')

    name_form = NameInputForm()
    class_race_form = ClassRaceForm()
    ab_score_form = AbilityScoreForm()
    background_form = BackgroundForm()
    

    if request.method != 'POST': # If a form has not been submitted yet, i.e, it is the first part
        return HttpResponse( #name entry 
                nameentry.render(
                    RequestContext( request, {
                        "name_form" : name_form,
                    } )
                )
            )        

    else: #not first step
        if "name_submit_button" in request.POST: #if the last thing submitted was the name
            name_form = NameInputForm(request.POST)
            if name_form.is_valid(): #name input form has been filled out

                #create a new row in the user_entry table
                character_in_progress = user_entry( name = name_form.cleaned_data['name'] )
                character_in_progress.save()
                character_in_progress = user_entry.objects.get(name__iexact = name_form.cleaned_data['name'] )

                #create a class_race_form and populate it with the initial data of the name
                class_race_form = ClassRaceForm(initial={'name': character_in_progress.name})

                return HttpResponse(
                    classrace.render(
                            RequestContext( request, {
                                "name_form": character_in_progress.name, 
                                "class_race_form": class_race_form
                            } )
                        )
                )

            else:
                return HttpResponse("You just submitted the name form, but it's not valid.")

        elif "class_race_submit_button" in request.POST: #if the last thing submitted was class and race
            class_race_form = ClassRaceForm(request.POST)
            if class_race_form.is_valid():

                character_in_progress = user_entry.objects.get(name__iexact = class_race_form.cleaned_data['name'] )
                character_in_progress.char_class = class_race_form.cleaned_data["character_class"]
                character_in_progress.race = class_race_form.cleaned_data["race"]
                character_in_progress.save()

                ab_score_form = AbilityScoreForm(initial={'name': character_in_progress.name})

                return HttpResponse(
                    abilityscores.render(
                        RequestContext( request, {
                                "ab_score_form": ab_score_form
                            } )
                        )
                )
            else:
                return HttpResponse("<p>You just submitted the class/race form, but it's not valid.</p>" + 
                    "<p>The errors were</p>" + str(class_race_form.errors) )

        elif "ability_scores_submit_button" in request.POST:
            ab_score_form = AbilityScoreForm(request.POST)
            if ab_score_form.is_valid():

                character_in_progress = user_entry.objects.get(name__iexact = ab_score_form.cleaned_data['name'] )
                character_in_progress.strength = ab_score_form.cleaned_data['strength']
                character_in_progress.dexterity = ab_score_form.cleaned_data['dexterity']
                character_in_progress.constitution = ab_score_form.cleaned_data['constitution']
                character_in_progress.intelegence = ab_score_form.cleaned_data['intelligence'] 
                #this is not a typo, it's misspelled in the models.py
                character_in_progress.wisdom = ab_score_form.cleaned_data['wisdom']
                character_in_progress.charisma = ab_score_form.cleaned_data['charisma']
                character_in_progress.save()


                background_form = BackgroundForm(initial={'name': character_in_progress.name})




# ============== do pdf stuff here ===========================================================================
                c = Character(character_in_progress.name,
                              character_in_progress.char_class,
                              character_in_progress.race,
                              character_in_progress.backround,
                              {"strength":int(character_in_progress.strength),
                               "dexterity":int(character_in_progress.dexterity),
                               "constitution":int(character_in_progress.constitution),
                               "intelligence":int(character_in_progress.intelegence),
                               "wisdom":int(character_in_progress.wisdom),
                               "charisma":int(character_in_progress.charisma)})
                pdftest.fill_pdf(c)
                path = os.path.abspath('..')+'/oursite/chargen/charactergen.pdf'
                with open(path, 'r') as pdf:
                    response = HttpResponse(pdf.read(), mimetype='application/pdf')
                    response['Content-Disposition'] = 'inline;filename=mycharacter.pdf'
                    return response
                pdf.closed
"""
                # return HttpResponse(
                #     background.render(
                #         RequestContext( request, {
                #             "background_form": background_form
                #         })
                #     )
                # )



            else:
                return HttpResponse("You had errors in your ability score form." + 
                    "They were: " + str(ab_score_form.errors))

        else:
            return HttpResponse("Something broke!")


"""
