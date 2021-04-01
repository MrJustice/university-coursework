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

        if filter_by_type:
            items = [item for item in self.queryset if item.type in filter_by_type]
            self.queryset = items
        if filter_by_cousine:
            items = [item for item in self.queryset if item.cousine in filter_by_cousine]
            self.queryset = items
        
        serializer = serializers.FoodEstablishmentSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = {"message": "Success."}
        return Response(data, content_type='application/json')

    def retrieve(self, request, pk=None):
        queryset = models.FoodEstablishment.objects.get(pk=pk)
        serializer = serializers.FoodEstablishmentSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = {"message": "Success."}
        return Response(data, content_type='application/json')

    def destroy(self, request, pk=None):
        pass

    @staticmethod
    @api_view(['GET'])
    def get_high_rated(request):
        queryset = models.FoodEstablishment.objects.order_by('-rating')[:3]
        serializer = serializers.FoodEstablishmentHomeScreenSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
