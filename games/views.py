from django.shortcuts import render
from django.views.generic import TemplateView

class ViewGame(TemplateView):

    template_name = 'game/2d_game.html'
