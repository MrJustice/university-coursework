from django.db.models import Q
from django.http import JsonResponse
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
        queryset = self.queryset.get(id=pk)
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
