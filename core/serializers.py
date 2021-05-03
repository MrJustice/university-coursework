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
    cousine = serializers.CharField(source='get_cousine_display', read_only=True)
    tables = TableSerializer(many=True)

    class Meta:
        model = FoodEstablishment
        fields = ['id', 'owner', 'title', 'description', 'rating', 'phone', 'cousine', 'average_check', 'location', 'email',
                  'working_hours', 'tables', 'full_title']

    def get_working_hours(self, obj):
        return self.get_working_hours

    def get_full_title(self, obj):
        return self.full_title


class FoodEstablishmentHomeScreenSerializer(serializers.ModelSerializer):
    cousine = serializers.CharField(source='get_cousine_display', read_only=True)

    class Meta:
        model = FoodEstablishment
        fields = ['id', 'cousine', 'average_check', 'location', 'rating', 'phone', 'working_hours', 'full_title']

    def get_working_hours(self, obj):
        return self.get_working_hours
    
    def get_full_title(self, obj):
        return self.full_title


class GuestFoodEstablishmentM2MSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    food_establishment = FoodEstablishmentSerializer()

    class Meta:
        model = GuestFoodEstablishmentM2M
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    guest_food_establishment = GuestFoodEstablishmentM2MSerializer()
    table = TableSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'