from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def products(request):
    return HttpResponse("Products. You're at products page.")