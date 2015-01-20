# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'dRace.south_works'
        db.add_column(u'chargen_drace', 'south_works',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'dRace.south_works'
        db.delete_column(u'chargen_drace', 'south_works')


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
            'south_works': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'str_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tool_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'weapon_proficiencies': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'wis_mod': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'chargen.dsub_class': {
            'Meta': {'object_name': 'dsub_class'},
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
        'chargen.spell': {
            'Meta': {'object_name': 'spell'},
            'char_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dChar_class']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_cantrips': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level1': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level18': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level2': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level3': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level4': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level5': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level6': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level7': ('django.db.models.fields.IntegerField', [], {}),
            'known_spell_level9': ('django.db.models.fields.IntegerField', [], {}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'minium_1st_level_spells': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level1': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level2': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level3': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level4': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level5': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level6': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level7': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level8': ('django.db.models.fields.IntegerField', [], {}),
            'possible_spells_level9': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level1': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level2': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level3': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level4': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level5': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level6': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level7': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level8': ('django.db.models.fields.IntegerField', [], {}),
            'slots_or_prepered_spell_level9': ('django.db.models.fields.IntegerField', [], {}),
            'sub_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dsub_class']"}),
            'total_spells': ('django.db.models.fields.IntegerField', [], {})
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
            'sub_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chargen.dsub_class']"}),
            'wisdom': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['chargen']