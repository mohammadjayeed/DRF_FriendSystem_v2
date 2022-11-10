from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserAdminConfig(UserAdmin):
    
    ordering = ('start_date',)
    
    list_display = ('email','id','user_name','is_active','is_staff','otp')

    fieldsets = (
        (None,{'fields':('email','user_name','otp')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser')}),
    )

    add_fieldsets = (
        (None,{
        'classes':('wide',),
        'fields':('email','user_name','password1','password2','is_staff','is_active'),
    }),

    )



admin.site.register(User, UserAdminConfig)