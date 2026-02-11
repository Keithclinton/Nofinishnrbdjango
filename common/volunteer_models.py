from django.db import models

class VolunteerApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    occupation = models.CharField(max_length=100)
    experience = models.TextField()
    availability = models.CharField(max_length=200)
    motivation = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.email})"
