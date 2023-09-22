from django.urls import path
from .import views


urlpatterns = [
    path('test/',views.test),
    path('',views.index),
    path('guard/',views.guard,name="guard"),
    path('about/',views.about,name="about"),
]