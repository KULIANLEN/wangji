from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create),
    path('submit/', views.submit),
    path('start_cp/', views.start_cp),
    path('query/<int:id>/<str:member_name>', views.query_member),
    path('query/<int:id>/', views.query),
]