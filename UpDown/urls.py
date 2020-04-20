from django.urls import path
from UpDown import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upScoreClientnum/', views.upScoreClientnum),
    path('checkRank/', views.checkRank),
]
