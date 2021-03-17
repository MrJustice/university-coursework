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

@api_view(['GET'])
def api_overview(request):
    queryset = models.User.objects.all()
    serializer = serializers.BasicUserSerializer(queryset, many=True)
    return Response(serializer.data)


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
        queryset = models.FoodEstablishment.objects.all()
        food_establishment = get_object_or_404(queryset, pk=pk)
        serializer = serializers.FoodEstablishmentSerializer(food_establishment)
        return Response(serializer.data)

    def update(self, request, pk=None):
        data = {"message": "Success."}
        return Response(data, content_type='application/json')

    def destroy(self, request, pk=None):
        pass