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
        queryset = dChar_class.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateClassDescription()'
        })
    )
    race = forms.ModelChoiceField(
        queryset = dRace.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateRaceDescription()'
            })
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

class BackgroundForm(forms.Form):
    background = forms.ModelChoiceField(
        queryset = dbackstory.objects.all(),
        widget = forms.Select(attrs = {
            "onChange": 'updateBackgroundDescription()'
        })
    )

class SubclassForm(forms.Form):
    subclass = forms.ModelChoiceField(
        queryset = dsubclass.objects.all()
    )



def index(request):
    allform = loader.get_template('chargen/allform.html')

    name_form = NameInputForm( prefix = "name_form" )
    class_race_form = ClassRaceForm( prefix = "class_race_form" )
    ab_score_form = AbilityScoreForm( prefix = "ab_score_form" )
    background_form = BackgroundForm( prefix = "background_form" )
    subclass_form = SubclassForm( prefix = "subclass_form" )
    
    if request.method != 'POST': 
        return HttpResponse(
                allform.render(
                    RequestContext( request, {
                        "name_form" : name_form,
                        "class_race_form" : class_race_form,
                        "ab_score_form" : ab_score_form,
                        "background_form": background_form,
                        "subclass_form": subclass_form,
                    } )
                )
            )        

    else:
        name_form = NameInputForm( request.POST, prefix="name_form")
        class_race_form = ClassRaceForm( request.POST, prefix = "class_race_form")
        ab_score_form = AbilityScoreForm( request.POST, prefix = "ab_score_form")
        background_form = BackgroundForm( request.POST, prefix = "background_form")
        subclass_form = SubclassForm( request.POST, prefix = "subclass_form")

        if all([
            name_form.is_valid(),
            class_race_form.is_valid(),
            ab_score_form.is_valid(),
            background_form.is_valid(),
            subclass_form.is_valid()
        ]):


            c = Character(name_form.cleaned_data["name"],
                        class_race_form.cleaned_data["character_class"].name,
                        "",
                        class_race_form.cleaned_data["race"].name,
                        background_form.cleaned_data["background"].name,
                        int(ab_score_form.cleaned_data["strength"]),
                        int(ab_score_form.cleaned_data["dexterity"]),
                        int(ab_score_form.cleaned_data["constitution"]),
                        int(ab_score_form.cleaned_data["intelligence"]),
                        int(ab_score_form.cleaned_data["wisdom"]),
                        int(ab_score_form.cleaned_data["charisma"]),
                        )

            return pdftest.fill_pdf(c)


        else:
            return HttpResponse("<p>Sorry, something went wrong. Our system found errors in your form.</p>" + 
                "<p>Those errors were: </p>" + 
                str(name_form.errors) + 
                str(class_race_form.errors) + 
                str(ab_score_form.errors) + 
                str(background_form.errors) + 
                str(subclass_form.errors)
                )

