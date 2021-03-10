from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse

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
    serializer = serializers.UserSerializer(queryset, many=True)
    return Response(serializer.data)