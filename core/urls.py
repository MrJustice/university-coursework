from rest_framework import routers
from django.conf.urls import url, include

from . import views

router = routers.SimpleRouter()
router.register(r'food-establishment', views.FoodEstablishmentViewSet)

urlpatterns = [
    url('', include(router.urls)),
]