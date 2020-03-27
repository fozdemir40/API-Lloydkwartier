from django.shortcuts import render
from rest_framework import viewsets
from .models import Lobby, Moves
from .serializers import LobbySerializer

# Create your views here.
class LobbyView (viewsets.ModelViewSet):
    queryset = Lobby.objects.all()
    serializer_class = LobbySerializer


