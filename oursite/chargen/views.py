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

from models import dChar_class, dRace, user_entry

def pdf_view(request):
    with open('myfile.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'filename=mycharacter.pdf'
        return response
    pdf.closed

class NameInputForm(forms.Form):
    nameinput = forms.CharField()
    progress = forms.CharField(
        initial="entering name",
        widget = forms.TextInput(attrs = {
            "type": "hidden"
            }
        )
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

class ClassRaceForm(forms.Form):
    character_class = forms.ModelMultipleChoiceField(
        queryset = dChar_class.objects.all(), 
        widget = forms.Select()
        )
    race = forms.ModelMultipleChoiceField(
        queryset = dRace.objects.all(), 
        widget = forms.Select()
        )



def index(request):
    index = loader.get_template('chargen/index.html')
    nameentry = loader.get_template('chargen/nameentry.html')
    classrace = loader.get_template('chargen/classrace.html')
    abilityscores = loader.get_template('chargen/abilityscores.html')

    name_form = NameInputForm()
    class_race_form = ClassRaceForm()
    ab_score_form = AbilityScoreForm()
    

    if request.method != 'POST': # If a form has not been submitted yet, i.e, it is the first part
        return HttpResponse( #name entry 
                nameentry.render(
                    RequestContext( request, {
                        "name_form" : name_form,
                    } )
                )
            )        

    else: #not first step
        name_form = NameInputForm(request.POST)
        if name_form.is_valid():
            character_in_progress = user_entry(name = name_form.cleaned_data['nameinput'])
            character_in_progress.save()
            if name_form.cleaned_data['progress'] == "entering name":
                return HttpResponse(
                    classrace.render(
                            RequestContext( request, {
                                "name_form": name_form.cleaned_data['nameinput'],
                                "class_race_form": class_race_form
                            } )
                        )
                )

        else:
            return HttpResponse("Name form not valid")


