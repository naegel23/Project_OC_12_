from django.urls import path, include
from .views import UserViewSet, ClientViewSet, ContractViewSet, EventViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'contracts', ContractViewSet)
router.register(r'events', EventViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
