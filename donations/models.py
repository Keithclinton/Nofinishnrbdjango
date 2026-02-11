from django.db import models
from django.conf import settings

class Donation(models.Model):
	STATUS_CHOICES = (
		('pending', 'Pending'),
		('completed', 'Completed'),
		('failed', 'Failed'),
	)
	# user is now optional for anonymous donations
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='donations', null=True, blank=True)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	payment_method = models.CharField(max_length=20, blank=True)
	first_name = models.CharField(max_length=50, blank=True)
	last_name = models.CharField(max_length=50, blank=True)
	email = models.EmailField(blank=True)
	phone = models.CharField(max_length=20, blank=True)
	is_recurring = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, blank=True)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.email or self.user} - {self.amount} ({self.status})"
