from django.urls import path
from .import views
urlpatterns = [
    path('',views.home),
    path('login',views.loginfun),
    path('signin',views.signfun)
]