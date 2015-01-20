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


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django import forms
from django.db import models
from django.forms import ModelForm

from models import dChar_class, dRace, user_entry

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

class ClassRaceForm(forms.Form):
    character_class = forms.ModelMultipleChoiceField(
        queryset=dChar_class.objects.all(), 
        widget = forms.Select()
        )
    race = forms.ModelMultipleChoiceField(
        queryset=dRace.objects.all(), 
        widget = forms.Select()
        )



def index(request):
    index = loader.get_template('chargen/index.html')
    classrace = loader.get_template('chargen/classrace.html')
    abilityscores = loader.get_template('chargen/abilityscores.html')

    ab_score_form = AbilityScoreForm()
    classraceform = ClassRaceForm()


    if request.method != 'POST': # If a form has not been submitted yet, i.e, it is the first part
        return HttpResponse(
                classrace.render(
                    RequestContext( request, {
                        "classraceform" : classraceform,
                    } )
                )
            )        


    else: # If the form has been submitted...
        ab_score_form = AbilityScoreForm(request.POST) # A form bound to the POST data

        if ab_score_form.is_valid(): # All validation rules pass
            strength = ab_score_form.cleaned_data["strength"]
            dexterity = ab_score_form.cleaned_data["dexterity"]
            constitution = ab_score_form.cleaned_data["constitution"]
            intelligence = ab_score_form.cleaned_data["intelligence"]
            wisdom = ab_score_form.cleaned_data["wisdom"]
            charisma = ab_score_form.cleaned_data["charisma"]
            return HttpResponse(
                "<p> You have submitted the form. Your ability scores are:</p>" + 
                "<p>Strength: " + str(int(strength)) + "</p>" +
                "<p>Dexterity: " + str(int(dexterity)) + "</p>" +
                "<p>Constitution: " + str(int(constitution)) + "</p>" +
                "<p>Intelligence: " + str(int(intelligence)) + "</p>" +
                "<p>Wisdom: " + str(int(wisdom)) + "</p>" +
                "<p>Charisma: " + str(int(charisma)) + "</p>"
                )

        else:
            ab_score_form = AbilityScoreForm() # An unbound form

    return HttpResponse(
            template.render(
                RequestContext( request, {
                'ab_score_form': ab_score_form
                } )
            )
        )

