from .models import *
from rest_framework import serializers


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = ['id', 'username', 'email']


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'


class FoodEstablishmentSerializer(serializers.ModelSerializer):
    owner = BasicUserSerializer()
    guests = GuestSerializer(many=True)

    class Meta:
        model = FoodEstablishment
        fields = ['owner', 'title', 'phone', 'location', 'email', 'number_of_tables', 'guests']


class FoodEstablishmentHomeScreenSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)
    cousine = serializers.CharField(source='get_cousine_display', read_only=True)

    class Meta:
        model = FoodEstablishment
        fields = ['id', 'type', 'title', 'cousine', 'average_check', 'location', 'rating', 'phone']


class GuestFoodEstablishmentM2MSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    food_establishment = FoodEstablishment()

    class Meta:
        model = GuestFoodEstablishmentM2M
        fileds = ['guest', 'food_establishment', 'member_since', 'number_of_visits']


class TableSerializer(serializers.ModelSerializer):
    food_establishment = FoodEstablishment()

    class Meta:
        model = Table
        fields = ['food_establishment', 'number', 'number_of_seats', 'smoke', 'status']


class ReservationSerializer(serializers.ModelSerializer):
    guest_food_establishment = GuestFoodEstablishmentM2MSerializer()

    class Meta:
        model = Reservation
        fields = ['guest_food_establishment', 'number_of_persons', 'start_date', 'end_date']