from django.contrib import admin
from .models import User, IndividualRegistration

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined')
	search_fields = ('email', 'first_name', 'last_name')
	list_filter = ('role', 'is_active', 'is_staff')

admin.site.register(IndividualRegistration)
