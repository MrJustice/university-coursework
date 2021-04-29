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


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class FoodEstablishmentSerializer(serializers.ModelSerializer):
    owner = BasicUserSerializer()
    type = serializers.CharField(source='get_type_display', read_only=True)
    cousine = serializers.CharField(source='get_cousine_display', read_only=True)
    tables = TableSerializer(many=True)

    class Meta:
        model = FoodEstablishment
        fields = ['id', 'owner', 'title', 'description', 'rating', 'phone', 'cousine', 'average_check', 'location',
                  'email', 'type', 'working_hours', 'tables']

    def get_working_hours(self, obj):
        return self.get_working_hours


class FoodEstablishmentHomeScreenSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)
    cousine = serializers.CharField(source='get_cousine_display', read_only=True)
    tables = TableSerializer(many=True)

    class Meta:
        model = FoodEstablishment
        fields = ['id', 'type', 'title', 'cousine', 'average_check', 'location', 'rating', 'phone', 'working_hours',
                  'tables']

    def get_working_hours(self, obj):
        return self.get_working_hours


class GuestFoodEstablishmentM2MSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    food_establishment = FoodEstablishment()

    class Meta:
        model = GuestFoodEstablishmentM2M
        fileds = ['guest', 'food_establishment', 'member_since', 'number_of_visits']


class ReservationSerializer(serializers.ModelSerializer):
    guest_food_establishment = GuestFoodEstablishmentM2MSerializer()

    class Meta:
        model = Reservation
        fields = ['guest_food_establishment', 'number_of_persons', 'start_date', 'end_date']