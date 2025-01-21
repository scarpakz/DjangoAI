from django.urls import path
from .views import index, groq_main_search

app_name="dashboard"

urlpatterns = [
    path('', index, name="dashboard"),
    path('text/', groq_main_search, name="text-search"),
]