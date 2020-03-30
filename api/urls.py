from django.urls import path, include
from . import views
from rest_framework import routers

router = views.MyRouter()
router.register('lobby', views.LobbyView)
router.register('moves', views.MovesView)

urlpatterns = [
    path('', include(router.urls)),
    path('bundle/', views.BundleView.as_view(), name="bundle"),
]