# urls.py

from django.urls import path
from .views import set_url_data_view

urlpatterns = [
    path('set-url-data/', set_url_data_view, name='set_url_data'),
    # Add other URL patterns as needed
]
