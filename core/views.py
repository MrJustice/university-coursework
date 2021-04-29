import datetime
from django.db.models import Q
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from . import models, serializers


class FoodEstablishmentViewSet(viewsets.ViewSet):
    queryset = models.FoodEstablishment.objects.all()
    serializer_class = serializers.FoodEstablishmentSerializer

    def list(self, request, *args, **kwargs):
        filter_by_type = request.query_params.getlist('filter_by_type[]')
        filter_by_cousine = request.query_params.getlist('filter_by_cousine[]')
        filter_by_price = request.query_params.getlist('filter_by_price[]')

        if filter_by_type:
            items = [item for item in self.queryset if item.type in filter_by_type]
            self.queryset = items
        if filter_by_cousine:
            items = [item for item in self.queryset if item.cousine in filter_by_cousine]
            self.queryset = items
        if filter_by_price:
            prices = []
            for price in filter_by_price:
                for item in list(map(int, price.split(','))):
                    prices.append(item)
            min_price, max_price = min(prices), max(prices)
            items = self.queryset.filter(Q(average_check__gte=min_price) & Q(average_check__lte=max_price))
            self.queryset = items

        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = {"message": "Success."}
        return Response(data, content_type='application/json')

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            queryset = self.queryset.get(id=pk)
        except models.FoodEstablishment.DoesNotExist:
            raise Http404
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        data = {"message": "Success."}
        return Response(data, content_type='application/json')

    def destroy(self, request, pk=None, *args, **kwargs):
        pass

    @staticmethod
    @api_view(['GET'])
    def get_high_rated(request):
        queryset = models.FoodEstablishment.objects.order_by('-rating')[:3]
        serializer = serializers.FoodEstablishmentHomeScreenSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['POST'])
    def reserve(request):
        guest_name = request.data.get("name")
        guest_phone = request.data.get("phone")
        number_of_persons = request.data.get("numberOfPersons")
        guest_table = request.data.get("table")
        guest_date = request.data.get("date")
        guest_time = request.data.get("time")
        guest_dt = datetime.datetime.strptime(
            guest_date + " " + guest_time, "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)

        restaurant = models.FoodEstablishment.objects.get(id=request.data.get('restaurant'))
        guest = models.Guest.objects.get_or_create(first_name=guest_name, phone=guest_phone)[0]
        
        try:
            m2m = models.GuestFoodEstablishmentM2M.objects.get(guest=guest, food_establishment=restaurant)
            m2m.increment_number_of_visits()
            m2m.save()
        except models.GuestFoodEstablishmentM2M.DoesNotExist:
            m2m = models.GuestFoodEstablishmentM2M.objects.create(
                guest=guest,
                food_establishment=restaurant,
                member_since=guest_date,
                number_of_visits=1
            )

        reservation = models.Reservation.objects.create(
            guest_food_establishment=m2m,
            number_of_persons=number_of_persons,
            start_date=guest_dt,
            table=guest_table
        )
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    def get_list_of_reservations(request):
        pass
