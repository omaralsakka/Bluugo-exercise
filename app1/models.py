from django.db import models

class File(models.Model):
	file = models.FileField(upload_to='uploads/')

class CarModel(models.Model):
	model_year = models.CharField(max_length=300)
	make = models.CharField(max_length=300)
	model = models.CharField(max_length=300)
	rejection_percentage = models.CharField(max_length=300)
	reason_1 = models.CharField(max_length=300)
	reason_2 = models.CharField(max_length=300)
	reason_3 = models.CharField(max_length=300)