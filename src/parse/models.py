from django.db import models

class Details(models.Model):
	id = models.AutoField(primary_key=True)
	salary = models.TextField()
	company = models.TextField()
	address = models.TextField()
	rules = models.TextField()
	description = models.TextField()