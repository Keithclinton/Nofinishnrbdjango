from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_id', 'status', 'created_at')
    search_fields = ('user__email', 'transaction_id')
    list_filter = ('status',)
