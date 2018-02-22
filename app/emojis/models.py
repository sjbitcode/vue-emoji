import uuid

from django.db import models
from django.utils import timezone


class Person(models.Model):
	name = models.CharField(max_length=10)
	age = models.IntegerField()

	def __str__(self):
		return '{} ({})'.format(self.name, self.age)