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

    def create(self, validated_data):
        sales_contact = self.context['request'].user
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        phone = validated_data['phone']
        mobile = validated_data['mobile']
        company_name = validated_data['company_name']
        is_confirmed_client = validated_data['is_confirmed_client']
        client_obj = Client(sales_contact=sales_contact,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone=phone,
                            mobile=mobile,
                            company_name=company_name,
                            is_confirmed_client=is_confirmed_client)
        client_obj.save()
        return validated_data


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


class SupportContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
