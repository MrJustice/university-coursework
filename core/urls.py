from rest_framework import routers
from django.conf.urls import url, include

from . import views

router = routers.SimpleRouter()
router.register(r'food-establishment', views.FoodEstablishmentViewSet)

urlpatterns = [
    url('', include(router.urls)),

    #Food establisments
    url('get-high-rated/', views.FoodEstablishmentViewSet.get_high_rated, name='get_high_rated'),
    url('reserve/', views.FoodEstablishmentViewSet.reserve, name='reserve'),
    url('get-reservations/', views.FoodEstablishmentViewSet.get_reservations, name='get_reservations'),
    url('guest-history/', views.guest_history, name='guest_history'),
    url('get-restaurant-reservations/', views.get_restaurant_reservations, name='get_restaurant_reservations'),
    url('restaurants-for-search/', views.get_restaurants_for_search, name='get_restaurants_for_search'),
]