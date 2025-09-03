from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Board
from .serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('-createdby')
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]
