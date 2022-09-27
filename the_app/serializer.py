from .models import CustomUser, Client, Contract, Event
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    is_confirmed_client = serializers.BooleanField(allow_null=True, default=False, required=False)

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id', 'sales_user', 'created_date', 'updated_date')


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date')


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date')
