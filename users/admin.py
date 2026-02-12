from django.contrib import admin
from .models import User, IndividualRegistration
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined')
	search_fields = ('email', 'first_name', 'last_name')
	list_filter = ('role', 'is_active', 'is_staff')
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'role')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'first_name', 'last_name', 'phone', 'role', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
	)
	ordering = ('email',)

admin.site.register(IndividualRegistration)
