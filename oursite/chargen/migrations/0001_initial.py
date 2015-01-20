# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'dWeapon'
        db.create_table(u'chargen_dweapon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weapon_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('martial_arts', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mele', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('finesse', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('damage_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('two_handed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('number_of_damage_die', self.gf('django.db.models.fields.IntegerField')()),
            ('type_of_damage_die', self.gf('django.db.models.fields.IntegerField')()),
            ('range_close', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('range_max', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('chargen', ['dWeapon'])

        # Adding model 'dRace'
        db.create_table(u'chargen_drace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('dex_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('char_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('str_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('int_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('wis_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('con_mod', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            ('skill_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('optional_skill_proficiencies', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('optional_lang_proficiencies', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weapon_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('armour_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tool_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('features', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dRace'])

        # Adding model 'dChar_class'
        db.create_table(u'chargen_dchar_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('hit_die', self.gf('django.db.models.fields.IntegerField')()),
            ('armour_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('weapon_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('tool_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('saving_throws_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('skill_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('number_skill_proficiencies', self.gf('django.db.models.fields.IntegerField')()),
            ('features', self.gf('django.db.models.fields.CharField')(max_length=3000)),
            ('cantrips_known', self.gf('django.db.models.fields.IntegerField')()),
            ('spells_known', self.gf('django.db.models.fields.IntegerField')()),
            ('spell_slots_1st_level', self.gf('django.db.models.fields.IntegerField')()),
            ('spell_casting_ability', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sugested_cantrips', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('sugested_1st_level_spells', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dChar_class'])

        # Adding model 'darmors'
        db.create_table(u'chargen_darmors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('armour_class', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ac_mod', self.gf('django.db.models.fields.IntegerField')()),
            ('strgenth_requirement', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('disadvantage_stealth', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('very_expensive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('moderatly_expensive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hellodarling', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('chargen', ['darmors'])

        # Adding model 'dbackstory'
        db.create_table(u'chargen_dbackstory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('skill_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('optional_lang_proficiencies', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tool_proficiencies', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('equipment', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dbackstory'])

        # Adding model 'dsubclass'
        db.create_table(u'chargen_dsubclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('char_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dChar_class'])),
            ('level_1_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_2_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_3_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_4_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_5_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_6_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_7_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_8_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_9_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_10_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_11_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_12_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_13_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_14_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_15_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_16_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_17_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_18_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_19_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('level_20_feature', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('chargen', ['dsubclass'])

        # Adding model 'user_entry'
        db.create_table(u'chargen_user_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('char_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dChar_class'])),
            ('sub_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dsubclass'])),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dRace'])),
            ('strgenth', self.gf('django.db.models.fields.IntegerField')()),
            ('dexterity', self.gf('django.db.models.fields.IntegerField')()),
            ('constitution', self.gf('django.db.models.fields.IntegerField')()),
            ('intelegence', self.gf('django.db.models.fields.IntegerField')()),
            ('wisdom', self.gf('django.db.models.fields.IntegerField')()),
            ('charisma', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('backround', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dbackstory'])),
        ))
        db.send_create_signal('chargen', ['user_entry'])

        # Adding model 'dspell'
        db.create_table(u'chargen_dspell', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('char_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dChar_class'])),
            ('sub_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chargen.dsubclass'])),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('slots_or_prepered_spell_level1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level5', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level6', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level7', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level8', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('slots_or_prepered_spell_level9', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level5', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level6', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level7', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level8', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('possible_spells_level9', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cantrips_known', self.gf('django.db.models.fields.IntegerField')()),
            ('total_spells', self.gf('django.db.models.fields.IntegerField')()),
            ('minium_1st_level_spells', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('chargen', ['dspell'])


    def backwards(self, orm):
        # Deleting model 'dWeapon'
        db.delete_table(u'chargen_dweapon')

        # Deleting model 'dRace'
        db.delete_table(u'chargen_drace')

        # Deleting model 'dChar_class'
        db.delete_table(u'chargen_dchar_class')

        # Deleting model 'darmors'
        db.delete_table(u'chargen_darmors')

        # Deleting model 'dbackstory'
        db.delete_table(u'chargen_dbackstory')

        # Deleting model 'dsubclass'
        db.delete_table(u'chargen_dsubclass')

        # Deleting model 'user_entry'
        db.delete_table(u'chargen_user_entry')

        # Deleting model 'dspell'
        db.delete_table(u'chargen_dspell')


    models = {
        'chargen.darmors': {
            'Meta': {'object_name': 'darmors'},
            'ac_mod': ('django.db.models.fields.IntegerField', [], {}),
            'armour_class': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'disadvantage_stealth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hellodarling': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
        'chargen.dchar_class': {
            'Meta': {'object_name': 'dChar_class'},
            'armour_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cantrips_known': ('django.db.models.fields.IntegerField', [], {}),
            'features': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
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
        'chargen.dspell': {
            'Meta': {'object_name': 'dspell'},
            'cantrips_known': ('django.db.models.fields.IntegerField', [], {}),
            'char_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dChar_class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'minium_1st_level_spells': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level7': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level8': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'possible_spells_level9': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level7': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level8': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slots_or_prepered_spell_level9': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sub_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dsubclass']"}),
            'total_spells': ('django.db.models.fields.IntegerField', [], {})
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
            'type_of_damage_die': ('django.db.models.fields.IntegerField', [], {}),
            'weapon_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'chargen.user_entry': {
            'Meta': {'object_name': 'user_entry'},
            'backround': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dbackstory']"}),
            'char_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dChar_class']"}),
            'charisma': ('django.db.models.fields.IntegerField', [], {}),
            'constitution': ('django.db.models.fields.IntegerField', [], {}),
            'dexterity': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intelegence': ('django.db.models.fields.IntegerField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dRace']"}),
            'strgenth': ('django.db.models.fields.IntegerField', [], {}),
            'sub_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dsubclass']"}),
            'wisdom': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['chargen']