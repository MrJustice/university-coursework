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

    def list(self, request):
        queryset = models.FoodEstablishment.objects.all()
        serializer = serializers.FoodEstablishmentSerializer(queryset, many=True)
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
        queryset = models.FoodEstablishment.objects.order_by('-rating')[:4]
        serializer = serializers.FoodEstablishmentHomeScreenSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
