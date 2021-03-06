from django.urls import path
from .views import *

urlpatterns = [
    path('', EventSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', EventSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'delete', 'options': 'options'})),
    path('authorize/', AuthorizeSet.as_view({'post': 'authorize'})),
    path('register/', RegisterSet.as_view({'post': 'register'})),
]