from django.contrib import admin

from .models import CustomUser, Client, Contract, Event


class UserFields(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'role']


class ClientFields(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'is_confirmed_client']


class ContractFields(admin.ModelAdmin):
    list_display = ['client', 'name', 'amount', 'is_signed']


class EventFields(admin.ModelAdmin):
    list_display = ['name', 'client', 'description', 'guests_number', 'created_date', 'event_status']


admin.site.register(CustomUser, UserFields)
admin.site.register(Client, ClientFields)
admin.site.register(Contract, ContractFields)
admin.site.register(Event, EventFields)
