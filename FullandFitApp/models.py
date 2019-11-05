from django.db import models

# Create your models here.

class Carls(models.Model): 
	item = models.CharField(max_length=120) 
	id = models.IntegerField(primary_key=True)
	price = models.FloatField()
	calories = models.FloatField()
	carbs = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
	
class TacoBell(models.Model): 
	item = models.CharField(max_length=120) 
	id = models.IntegerField(primary_key=True)
	price = models.FloatField()
	calories = models.FloatField()
	carbs = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()	
	
class Den(models.Model): 
	item = models.CharField(max_length=120) 
	id = models.IntegerField(primary_key=True)
	price = models.FloatField()
	calories = models.FloatField()
	carbs = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
	
class RoundTable(models.Model): 
	item = models.CharField(max_length=120) 
	id = models.IntegerField(primary_key=True)
	price = models.FloatField()
	calories = models.FloatField()
	carbs = models.FloatField()
	protein = models.FloatField()
	fat = models.FloatField()
