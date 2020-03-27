import uuid

from django.db import models


# Create your models here.
class Moves(models.Model):
    Location1 = models.BigIntegerField(default=0)
    Location2 = models.BigIntegerField(default=0)


class Lobby(models.Model):
    Session = models.UUIDField(editable=False, default=uuid.uuid4().hex[:8])
    PersonOne = models.CharField(max_length=50, default='0')
    PersonTwo = models.CharField(max_length=50, default='0')
    LobbyCode = models.CharField(max_length=50, default='0')
    Moves = models.ForeignKey(Moves, on_delete=models.CASCADE)

    def __str__(self):
        return self.Session



