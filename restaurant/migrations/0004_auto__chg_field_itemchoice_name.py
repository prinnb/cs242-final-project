# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ItemChoice.name'
        db.alter_column(u'restaurant_itemchoice', 'name', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'ItemChoice.name'
        db.alter_column(u'restaurant_itemchoice', 'name', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        u'restaurant.businesshours': {
            'Meta': {'object_name': 'BusinessHours'},
            'close_time': ('django.db.models.fields.TimeField', [], {}),
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'open_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'restaurant.foodcategory': {
            'Meta': {'object_name': 'FoodCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'restaurant.fooditem': {
            'Meta': {'object_name': 'FoodItem'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'restaurant.foodmenu': {
            'Meta': {'object_name': 'FoodMenu'},
            'food_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.FoodCategory']"}),
            'food_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.FoodItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_cat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.MenuCategory']"}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        u'restaurant.itemchoice': {
            'Meta': {'object_name': 'ItemChoice'},
            'food_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.FoodItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.IntegerField', [], {}),
            'price_add': ('django.db.models.fields.FloatField', [], {})
        },
        u'restaurant.menucategory': {
            'Meta': {'object_name': 'MenuCategory'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'end_day': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_day': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'restaurant.restaurantinfo': {
            'Meta': {'object_name': 'RestaurantInfo'},
            'about_us': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'restaurant.suggestion': {
            'Meta': {'object_name': 'Suggestion'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['restaurant']