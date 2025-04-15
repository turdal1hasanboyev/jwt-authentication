from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


admin.site.site_header = "jwt-authentication Admin Panel"
admin.site.site_title = "jwt-authentication Admin Panel"
admin.site.index_title = "Welcome to jwt-authentication Admin Panel!"


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    search_fields = ('email',)
    list_display = (
        'id',
        'email',
        'is_active',
        'is_superuser',
        'is_staff',
        'last_login',
        'date_joined',
    )
    list_filter = (
        'is_active',
        'is_superuser',
        'is_staff',
    )
    fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff', 'is_active',),
        }),
        ("Important Dates", {
            'fields': ('date_joined', 'last_login',),
        }),
    )
    add_fieldsets = (
        ('Create Super User', {
            'fields': ('email', 'password1', 'password2',),
        }),
        ("Permissions", {
            'fields': ('is_superuser', 'is_staff',),
        }),
    )
