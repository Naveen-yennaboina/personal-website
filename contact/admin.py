from django.contrib import admin
from .views import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'contact_number', 'company_name', 'description']


admin.site.register(Users, UserAdmin)
