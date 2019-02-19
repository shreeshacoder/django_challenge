from django.urls import path

from . import views

urlpatterns = [
    path('', views.HouseDetailsList.as_view()),
    path('<int:pk>/', views.HouseDetailsDetail.as_view()),
    path('create/', views.CreateHouseDetailEntry.as_view())
]