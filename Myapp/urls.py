from django.contrib import admin
from django.urls import path
from Myapp import views
urlpatterns = [
    path('',views.index,name="index"),
    path('<str:final>', views.get_pass, name="Hasher")
]
