from django.urls import path
from . import views

urlpatterns = [
    path('withoutapi/', views.withoutapi),
    path('withoutapi/<int:pk>/', views.withoutapidetail),
    path('withapi/', views.withapi),
    path('withapi/<int:pk>/', views.withapidetail)
]