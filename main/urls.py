from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('kasb/', Kasb),
    path('add-kasb/', AddKasb),
    path('delete-kasb/<int:id>/', DeleteKasb),
    path('edit-kasb/', EditKasb),
    path('hodim/', Hodim),
]