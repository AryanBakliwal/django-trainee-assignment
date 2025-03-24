from django.urls import path
from thread_test import views

urlpatterns = [
    path('thread-test/', views.test_view, name='test-view'),
]
