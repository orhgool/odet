import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

def index(request):
	return render(request, 'tablero/index.html')   