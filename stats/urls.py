from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from stats import views

app_name = 'stats'


urlpatterns = [
    path('add_data/', views.add_sugar_data),
    path('login/', views.login_user),
    path('signup/', views.RegisterView.as_view())## убрать потом
]