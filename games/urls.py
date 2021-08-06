from django.urls import path
from .views import ViewGame
urlpatterns = [
    path('2d_game', ViewGame.as_view(), name='game'),
]