from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('alpaca-sma/', views.alpaca_sma_view, name='alpaca_sma')
]