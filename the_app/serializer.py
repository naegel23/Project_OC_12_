from .models import CustomUser, Client, Contract, Event
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    client = serializers.CharField(required=False)
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

    def validate(self, attrs):
        if self.context['request'].method == "POST":
            if Client.objects.filter(first_name=attrs['client']).exists():
                client = Client.objects.get(first_name=attrs['client'])
            else:
                raise serializers.ValidationError("There are no client with the first name : " + str(attrs['client']))

            if client.is_confirmed_client:
                pass
            else:
                raise serializers.ValidationError('This client is not a confirmed client yet')
        else:
            pass

        return attrs


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date')

    def validate(self, attrs):
        if self.context['request'].method == "POST":
            if Client.objects.filter(first_name=attrs['client']).exists():
                pass
            else:
                raise serializers.ValidationError("There are no client with the first name : " + str(attrs['client']))

            if Contract.objects.filter(name=attrs['contract']).exists():
                contract = Contract.objects.get(name=attrs['contract'])
            else:
                raise serializers.ValidationError("There are no contract with the name : " + str(attrs['contract']))

            if contract.is_signed:
                pass
            else:
                raise serializers.ValidationError('The event cannot be created until it\'s contract is signed')

        else:
            pass

        return attrs