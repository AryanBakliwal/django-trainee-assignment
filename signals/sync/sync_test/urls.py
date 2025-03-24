from django.urls import path
from . import views

urlpatterns = [
    path('sync-test/', views.test_view, name='test-view'),
]
