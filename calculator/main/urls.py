from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name="home"),
    path('',views.base, name ="base"),
    path('operation/', views.operation, name="operation")
]
