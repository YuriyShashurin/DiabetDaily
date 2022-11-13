from django.urls import path, include
from stats import views

app_name = 'stats'


urlpatterns = [
    path('add_data/', views.add_sugar_data),
    path('login/', views.login),
]