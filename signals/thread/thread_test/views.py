from django.shortcuts import render
from django.http import HttpResponse
from .models import TestModel
import threading

# Create your views here.

def test_view(request):
    print(f"View Caller Thread ID: {threading.get_ident()}")
    TestModel.objects.create(name="Test")
    return HttpResponse("Done")