
from django.db import models

class Sponsor(models.Model):
	STATUS_CHOICES = (
		('pending', 'Pending'),
		('approved', 'Approved'),
		('rejected', 'Rejected'),
	)
	name = models.CharField(max_length=100)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
