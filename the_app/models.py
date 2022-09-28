from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
# Create your models here.


class CustomUser(AbstractUser):
    roles = [('Gestion', 'Gestion'), ('Vente', 'Vente'), ('Support', 'Support')]
    role = models.CharField(choices=roles, max_length=255, default="Vente")

    def __str__(self):
        return self.username + " | " + "role: " + self.role


class SalesContact(models.Model):
    contact = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, limit_choices_to={'role': 'Vente'},
                                related_name="sale_contact", blank=True, null=True)


class SupportContact(models.Model):
    contact = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, limit_choices_to={'role': 'Support'},
                                related_name="support_user", blank=True, null=True)


class StaffContact(models.Model):
    contact = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, limit_choices_to={'role': 'Gestion'},
                                related_name="staff_contact", blank=True, null=True)


class EventStatus(models.Model):
    all_status = [('en cours', 'en cours'), ('terminé', 'terminé')]
    status = models.CharField(choices=all_status, max_length=255, default="en cours")

    def __str__(self):
        return self.status


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    is_confirmed_client = models.BooleanField(default=False)
    company_name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING,
                                      blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.first_name


class Contract(models.Model):
    name = models.CharField(max_length=255, unique=True)
    sales_contact = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_signed = models.BooleanField(default=False)
    amount = models.IntegerField(validators=[MinValueValidator(1)])
    objects = models.Manager()

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        try:
            self.client is not None
        except Client.DoesNotExist:
            raise ValidationError('A contract must have a client to be created')
        print(self.client)
        print(self.client.is_confirmed_client)
        if self.client.is_confirmed_client:
            return True
        else:
            raise ValidationError('This client is not a confirmed client yet')


class Event(models.Model):
    name = models.CharField(max_length=255)
    contract = models.ForeignKey(to=Contract, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=CustomUser, on_delete=models.DO_NOTHING, blank=True, null=True)
    event_status = models.ForeignKey(to=EventStatus, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255)
    guests_number = models.IntegerField(validators=[MinValueValidator(1)])
    objects = models.Manager()

    def __str__(self):
        return self.name

    def clean(self, *args, **kwargs):
        print(self.contract)
        print(self.contract.is_signed)
        if self.contract.is_signed:
            return True
        else:
            raise ValidationError('The event cannot be created until it\'s contract is signed')