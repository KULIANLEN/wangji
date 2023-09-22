from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create),
    path('modify/', views.modify),
    path('start_cp/', views.start_cp),
    path('query/<int:id>/', views.query),
]
