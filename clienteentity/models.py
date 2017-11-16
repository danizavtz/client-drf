from django.db import models


class Cliente(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	login = models.CharField(max_length=100, blank=True, default='')
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)

	class Meta:
		ordering = ('created',)