# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'dBackgroundDescription'
        db.delete_table(u'chargen_dbackgrounddescription')

        # Deleting model 'dClassDescription'
        db.delete_table(u'chargen_dclassdescription')

        # Deleting model 'dSubclassDescription'
        db.delete_table(u'chargen_dsubclassdescription')

        # Deleting model 'dRaceDescription'
        db.delete_table(u'chargen_dracedescription')

        # Adding model 'dDescription'
        db.create_table(u'chargen_ddescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dDescription'])


    def backwards(self, orm):
        # Adding model 'dBackgroundDescription'
        db.create_table(u'chargen_dbackgrounddescription', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('background', self.gf('django.db.models.fields.CharField')(max_length=40)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('chargen', ['dBackgroundDescription'])

        # Adding model 'dClassDescription'
        db.create_table(u'chargen_dclassdescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char_class', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dClassDescription'])

        # Adding model 'dSubclassDescription'
        db.create_table(u'chargen_dsubclassdescription', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('subclass', self.gf('django.db.models.fields.CharField')(max_length=40)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('chargen', ['dSubclassDescription'])

        # Adding model 'dRaceDescription'
        db.create_table(u'chargen_dracedescription', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=40)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('chargen', ['dRaceDescription'])

        # Deleting model 'dDescription'
        db.delete_table(u'chargen_ddescription')


    models = {
        'chargen.darmors': {
            'Meta': {'object_name': 'darmors'},
            'ac_mod': ('django.db.models.fields.IntegerField', [], {}),
            'armour_class': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'disadvantage_stealth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderatly_expensive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'strgenth_requirement': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'very_expensive': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'chargen.dbackstory': {
            'Meta': {'object_name': 'dbackstory'},
            'equipment': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'optional_lang_proficiencies': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'tool_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'chargen.dbonds': {
            'Meta': {'object_name': 'dbonds'},
            'background': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'five': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'four': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'one': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'six': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'three': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'two': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'chargen.dchar_class': {
            'Meta': {'object_name': 'dChar_class'},
            'armour_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantrips_known': ('django.db.models.fields.IntegerField', [], {}),
            'hit_die': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'number_skill_proficiencies': ('django.db.models.fields.IntegerField', [], {}),
            'saving_throws_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'skill_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'spell_casting_ability': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'spell_slots_1st_level': ('django.db.models.fields.IntegerField', [], {}),
            'spells_known': ('django.db.models.fields.IntegerField', [], {}),
            'sugested_1st_level_spells': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'sugested_cantrips': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'tool_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'weapon_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        'chargen.ddescription': {
            'Meta': {'object_name': 'dDescription'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'chargen.dflaws': {
            'Meta': {'object_name': 'dflaws'},
            'background': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'five': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'four': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'one': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'six': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'three': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'two': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'chargen.dideals': {
            'Meta': {'object_name': 'dideals'},
            'background': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'five': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'four': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'one': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'six': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'three': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'two': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'chargen.dpersonalities': {
            'Meta': {'object_name': 'dpersonalities'},
            'background': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'eight': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'five': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'four': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'one': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'seven': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'six': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'three': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'two': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'chargen.drace': {
            'Meta': {'object_name': 'dRace'},
            'armour_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'char_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'con_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dex_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'features': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'int_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'optional_lang_proficiencies': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'optional_skill_proficiencies': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skill_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'str_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tool_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'weapon_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'wis_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'chargen.dsubclass': {
            'Meta': {'object_name': 'dsubclass'},
            'char_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dChar_class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_10_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_11_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_12_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_13_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_14_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_15_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_16_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_17_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_18_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_19_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_1_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_20_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_2_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_3_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_4_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_5_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_6_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_7_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_8_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'level_9_feature': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'chargen.dweapon': {
            'Meta': {'object_name': 'dWeapon'},
            'damage_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'finesse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'martial_arts': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mele': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'number_of_damage_die': ('django.db.models.fields.IntegerField', [], {}),
            'range_close': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'range_max': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'two_handed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'two_handed_damage': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'type_of_damage_die': ('django.db.models.fields.IntegerField', [], {}),
            'versatile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'weapon_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['chargen']