from rest_framework import viewsets
from .models import CustomUser, Client, Contract, Event
from .serializer import UserSerializer, ClientSerializer, ContractSerializer, EventSerializer
from .permissions import Permissions, EventPermissions
from rest_framework import permissions
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, Permissions]
    queryset = Client.objects.all()

    def get_queryset(self):

        return Client.objects.filter(sales_contact__support=support)


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, Permissions]
    queryset = Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, EventPermissions]
    queryset = Event.objects.all()
