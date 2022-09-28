from rest_framework import viewsets
from .models import Client, Contract, Event
from .serializer import ClientSerializer, ContractSerializer, EventSerializer
from .permissions import Permissions, EventPermissions
from rest_framework import permissions
from rest_framework import filters
# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, Permissions]
    search_fields = ['first_name', 'email']
    filter_backends = (filters.SearchFilter,)
    queryset = Client.objects.all()


class ContractViewSet(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, Permissions]
    search_fields = ['client__first_name', 'client__email', 'created_date', 'amount']
    filter_backends = (filters.SearchFilter,)
    queryset = Contract.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, EventPermissions]
    search_fields = ['client__first_name', 'client__email', 'event_date']
    filter_backends = (filters.SearchFilter,)
    queryset = Event.objects.all()
