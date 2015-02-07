"""
This file controls which http responses and html pages are shown.

Functions here should take their input from urls.py and return an 
HttpResponse object.

More information at https://docs.djangoproject.com/en/1.6/intro/tutorial03/
or at https://docs.djangoproject.com/en/1.6/topics/http/views/
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

from models import dChar_class, dRace, dbackstory, dsubclass

#These are form outlines that are called in the index function.

class OneForm(forms.Form):
    name = forms.CharField(required = False)

    #These modelchoicefield objects are linked to rows in the dChar_class and dRace models, respectively.
    #Each row in the database becomes one select option here.
    character_class = forms.ModelChoiceField(
        queryset = dChar_class.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateClassDescription()'
        }),
        required=False
    )
    race = forms.ModelChoiceField(
        queryset = dRace.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateRaceDescription()'
            }),
        required= False
    )

    strength     = forms.ChoiceField(
        #This ugliness is necessary to provide the <select> with the correct range of values.
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

    subclass = forms.ModelChoiceField(
        queryset = dsubclass.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateSubclassDescription()'
        }),
        required = False
        )
    
    background = forms.ModelChoiceField(
        queryset = dbackstory.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateBackgroundDescription()'
        }),
        required = False
        )  


def index(request):
    """
    This function handles all requests from users.

    It doesn't need to store any user data because there are only two types of requests:
    1) not POST, to which it responds with a blank form, or
    2) POST, to which it responds with a pdf generated from the form data.
    """

    allform = loader.get_template('chargen/allform.html')
    
    one_form = OneForm()

    if request.method != 'POST': 
        return HttpResponse(
                allform.render(
                    RequestContext( request, {
                        "one_form": one_form,
                        #this is necessary so that the template knows which fields to render in the table
                        "ab_scores": ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"],
                    } )
                )
            )        

    else:
        one_form = OneForm(request.POST)
         
        if one_form.is_valid(): 

            if one_form.cleaned_data["race"]==None:
                race = ""
            else:
                race = one_form.cleaned_data["race"].name

            if one_form.cleaned_data["character_class"]==None:
                char_class = ""
                subclass = ""
            else:
                char_class = one_form.cleaned_data["character_class"].name
                if one_form.cleaned_data["subclass"]==None:
                    subclass = ""
                else:
                    #Not sure what this is for? Ask Rachel, I think,
                    #this is so that the proper subclass is passed. I can explain in person if you want
                    index = one_form.cleaned_data["subclass"].id
                    subclass = dsubclass.objects.filter(char_class = dChar_class.objects.get(name = one_form.cleaned_data["character_class"].name))[index-1].name

            if one_form.cleaned_data["background"]==None:
                background = ""
            else:
                background = one_form.cleaned_data["background"].name

            #Character is from character.py
            c = Character(one_form.cleaned_data["name"],
                        char_class,
                        subclass,
                        race,
                        background,
                        int(one_form.cleaned_data["strength"]),
                        int(one_form.cleaned_data["dexterity"]),
                        int(one_form.cleaned_data["constitution"]),
                        int(one_form.cleaned_data["intelligence"]),
                        int(one_form.cleaned_data["wisdom"]),
                        int(one_form.cleaned_data["charisma"]),
                        )

            #pdftest takes a character argument and returns a pdf file as an HttpResponse.
            return pdftest.fill_pdf(c)

        else:
            return HttpResponse("<p>Sorry, something went wrong. Our system found errors in your form.</p>" + 
                "<p>Those errors were: </p>" + 
                str(one_form.errors)
                )

