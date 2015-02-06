# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'dspell'
        db.delete_table(u'chargen_dspell')

        # Deleting model 'user_entry'
        db.delete_table(u'chargen_user_entry')

        # Adding model 'dBackgroundDescription'
        db.create_table(u'chargen_dbackgrounddescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('background', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dBackgroundDescription'])

        # Adding model 'dClassDescription'
        db.create_table(u'chargen_dclassdescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char_class', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dClassDescription'])

        # Adding model 'dRaceDescription'
        db.create_table(u'chargen_dracedescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dRaceDescription'])

        # Adding model 'dSubclassDescription'
        db.create_table(u'chargen_dsubclassdescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subclass', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dSubclassDescription'])


    def backwards(self, orm):
        # Adding model 'dspell'
        db.create_table(u'chargen_dspell', (
            ('total_spells', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('minium_1st_level_spells', self.gf('django.db.models.fields.IntegerField')()),
            ('char_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dChar_class'])),
            ('sub_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dsubclass'])),
            ('slots_or_prepered_spell_level3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level7', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level6', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level5', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level9', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level8', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('cantrips_known', self.gf('django.db.models.fields.IntegerField')()),
            ('possible_spells_level4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level5', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level6', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level7', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level8', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level9', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('chargen', ['dspell'])

        # Adding model 'user_entry'
        db.create_table(u'chargen_user_entry', (
            ('dexterity', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('sub_class', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chargen.dsubclass'])),
            ('strgenth', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('wisdom', self.gf('django.db.models.fields.IntegerField')(default=8)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('constitution', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('charisma', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('backround', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chargen.dbackstory'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chargen.dRace'])),
            ('intelegence', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('char_class', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['chargen.dChar_class'])),
        ))
        db.send_create_signal('chargen', ['user_entry'])

        # Deleting model 'dBackgroundDescription'
        db.delete_table(u'chargen_dbackgrounddescription')

        # Deleting model 'dClassDescription'
        db.delete_table(u'chargen_dclassdescription')

        # Deleting model 'dRaceDescription'
        db.delete_table(u'chargen_dracedescription')

        # Deleting model 'dSubclassDescription'
        db.delete_table(u'chargen_dsubclassdescription')


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
        'chargen.dbackgrounddescription': {
            'Meta': {'object_name': 'dBackgroundDescription'},
            'background': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'chargen.dclassdescription': {
            'Meta': {'object_name': 'dClassDescription'},
            'char_class': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
        'chargen.dracedescription': {
            'Meta': {'object_name': 'dRaceDescription'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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
        'chargen.dsubclassdescription': {
            'Meta': {'object_name': 'dSubclassDescription'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subclass': ('django.db.models.fields.CharField', [], {'max_length': '40'})
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