from rest_framework import serializers
from .models import Lobby, Moves


# Serializers here

class LobbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lobby
        fields = ('id', 'url', 'PersonOne', 'PersonTwo', 'LobbyCode')


class MovesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moves
        fields = ('url', 'Location1', 'Location2')
