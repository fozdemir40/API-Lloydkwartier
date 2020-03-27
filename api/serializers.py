from rest_framework import serializers
from .models import Lobby, Moves


# Serializers here

class LobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lobby
        fields = ('id', 'url', 'session', 'playerOne', 'playerTwo', 'lobbyCode', 'moves')


class MovesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moves
        fields = ('id', 'url', 'location1', 'location2')
