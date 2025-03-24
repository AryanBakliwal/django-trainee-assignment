from django.shortcuts import render
from django.http import HttpResponse
from .models import TestModel
import time

# Create your views here.

def test_view(request):
    start = time.time()
    TestModel.objects.create(name="Test")
    end = time.time()
    print(f"View execution time: {end - start} seconds")
    return HttpResponse("Done")
