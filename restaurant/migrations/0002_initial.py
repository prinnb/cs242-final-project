# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RestaurantInfo'
        db.create_table(u'restaurant_restaurantinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('about_us', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'restaurant', ['RestaurantInfo'])

        # Adding model 'BusinessHours'
        db.create_table(u'restaurant_businesshours', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('open_time', self.gf('django.db.models.fields.TimeField')()),
            ('close_time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'restaurant', ['BusinessHours'])

        # Adding model 'Suggestion'
        db.create_table(u'restaurant_suggestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'restaurant', ['Suggestion'])

        # Adding model 'MenuCategory'
        db.create_table(u'restaurant_menucategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('start_day', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('end_day', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('start_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'restaurant', ['MenuCategory'])

        # Adding model 'FoodCategory'
        db.create_table(u'restaurant_foodcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'restaurant', ['FoodCategory'])

        # Adding model 'FoodItem'
        db.create_table(u'restaurant_fooditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'restaurant', ['FoodItem'])

        # Adding model 'ItemChoice'
        db.create_table(u'restaurant_itemchoice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('food_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.FoodItem'])),
            ('price_add', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'restaurant', ['ItemChoice'])

        # Adding model 'FoodMenu'
        db.create_table(u'restaurant_foodmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('food_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.FoodItem'])),
            ('food_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.FoodCategory'])),
            ('menu_cat', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.MenuCategory'])),
            ('price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'restaurant', ['FoodMenu'])


    def backwards(self, orm):
        # Deleting model 'RestaurantInfo'
        db.delete_table(u'restaurant_restaurantinfo')

        # Deleting model 'BusinessHours'
        db.delete_table(u'restaurant_businesshours')

        # Deleting model 'Suggestion'
        db.delete_table(u'restaurant_suggestion')

        # Deleting model 'MenuCategory'
        db.delete_table(u'restaurant_menucategory')

        # Deleting model 'FoodCategory'
        db.delete_table(u'restaurant_foodcategory')

        # Deleting model 'FoodItem'
        db.delete_table(u'restaurant_fooditem')

        # Deleting model 'ItemChoice'
        db.delete_table(u'restaurant_itemchoice')

        # Deleting model 'FoodMenu'
        db.delete_table(u'restaurant_foodmenu')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
            'city': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
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