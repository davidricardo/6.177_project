"""
This file controls which http responses and html pages are shown.

Functions here should take their input from urls.py and return an 
HttpResponse object.

More information at https://docs.djangoproject.com/en/1.6/intro/tutorial03/
or at https://docs.djangoproject.com/en/1.6/topics/http/views/
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django import forms

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

def index(request):
    template = loader.get_template('chargen/index.html')

    if request.method == 'POST': # If the form has been submitted...
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
