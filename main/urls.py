from django.urls import path
from .views import index_view, create_contact

urlpatterns = [
    path('', index_view, name='index'),
    path('create-contact/', create_contact, name='create-contact'),
]