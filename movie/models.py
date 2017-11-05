from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=255)
	production_date = models.DateTimeField()
	director = models.CharField(max_length=128)
	def __str__(self):
		return self.title

	@property
	def clean_data_production(self):
		return self.production_date.date()
