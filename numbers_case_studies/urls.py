from django.urls import path
from number_to_english_app.views import num_to_english

urlpatterns = [
    path('num_to_english', num_to_english, name='num_to_english'),
]
