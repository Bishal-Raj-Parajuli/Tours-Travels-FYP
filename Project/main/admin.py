from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .userForms import UserCreationForm, UserChangeForm


from .models import Bookings, Destinations, Packages, Guides
# Register your models here.

class AccountAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'phone', 'date_of_birth', 'is_staff',  'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name', 'phone')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(CustomUser, AccountAdmin)

@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):
    list_display = ['name','address']

@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ['destination','price','days','persons','description','is_active']

@admin.register(Guides)
class GuidesAdmin(admin.ModelAdmin):
    list_display = ['name','address','contact','is_active']

@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['package','guide']
