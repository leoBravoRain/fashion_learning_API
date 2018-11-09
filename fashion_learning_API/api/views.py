# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):

	# Get the image
	image = request.POST["image"]

	# Se crea respuesta
	response = {"data": image}

	# Se envia respuesta
	return JsonResponse(response)
