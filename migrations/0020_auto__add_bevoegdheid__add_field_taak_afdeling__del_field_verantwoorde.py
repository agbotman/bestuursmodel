# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bevoegdheid'
        db.create_table(u'bestuursmodel_bevoegdheid', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naam', self.gf('django.db.models.fields.CharField')(unique=True, max_length=45)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
            ('afdeling', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='bevoegdheden', null=True, to=orm['bestuursmodel.Afdeling'])),
        ))
        db.send_create_signal(u'bestuursmodel', ['Bevoegdheid'])

        # Adding field 'Taak.afdeling'
        db.add_column(u'bestuursmodel_taak', 'afdeling',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='taken', null=True, to=orm['bestuursmodel.Afdeling']),
                      keep_default=False)

        # Removing M2M table for field rollen on 'Taak'
        db.delete_table(db.shorten_name(u'bestuursmodel_taak_rollen'))

        # Deleting field 'Verantwoordelijkheid.rol'
        db.delete_column(u'bestuursmodel_verantwoordelijkheid', 'rol_id')


    def backwards(self, orm):
        # Deleting model 'Bevoegdheid'
        db.delete_table(u'bestuursmodel_bevoegdheid')

        # Deleting field 'Taak.afdeling'
        db.delete_column(u'bestuursmodel_taak', 'afdeling_id')

        # Adding M2M table for field rollen on 'Taak'
        m2m_table_name = db.shorten_name(u'bestuursmodel_taak_rollen')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('taak', models.ForeignKey(orm[u'bestuursmodel.taak'], null=False)),
            ('rol', models.ForeignKey(orm[u'bestuursmodel.rol'], null=False))
        ))
        db.create_unique(m2m_table_name, ['taak_id', 'rol_id'])

        # Adding field 'Verantwoordelijkheid.rol'
        db.add_column(u'bestuursmodel_verantwoordelijkheid', 'rol',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='verantwoordelijkheden', null=True, to=orm['bestuursmodel.Rol'], blank=True),
                      keep_default=False)


    models = {
        u'bestuursmodel.afdeling': {
            'Meta': {'object_name': 'Afdeling'},
            'einddatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'}),
            'nummer': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'permanent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rapporteert_aan': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'commissies'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'to': u"orm['bestuursmodel.Sector']"}),
            'startdatum': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'taakbeschrijving': ('django.db.models.fields.TextField', [], {}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'bestuursmodel.bevoegdheid': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Bevoegdheid'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'bevoegdheden'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.functie': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Functie'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'functies'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.functieeis': {
            'Meta': {'ordering': "['naam']", 'object_name': 'FunctieEis'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'functies': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'functie_eisen'", 'symmetrical': 'False', 'to': u"orm['bestuursmodel.Functie']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.rol': {
            'Meta': {'object_name': 'Rol'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rollen'", 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {'default': "' '", 'null': 'True', 'blank': 'True'}),
            'functie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rollen'", 'to': u"orm['bestuursmodel.Functie']"}),
            'generieke_rol': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bestuursmodel.RolGeneriek']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'bestuursmodel.rolgeneriek': {
            'Meta': {'object_name': 'RolGeneriek'},
            'beschrijving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.sector': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Sector'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kleur': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.taak': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Taak'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'taken'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        },
        u'bestuursmodel.verantwoordelijkheid': {
            'Meta': {'ordering': "['naam']", 'object_name': 'Verantwoordelijkheid'},
            'afdeling': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'verantwoordelijkheden'", 'null': 'True', 'to': u"orm['bestuursmodel.Afdeling']"}),
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naam': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '45'})
        }
    }

    complete_apps = ['bestuursmodel']