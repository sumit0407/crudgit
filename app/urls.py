from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [

    path("",views.Index,name="index"),
    path("index1",views.index1,name="index1"),
    path("up/<int:pk>/",views.Up,name="up"),
    path("data",views.Data,name="data"),
    path("updatedata/<int:pk>/",views.updatedata,name="updatedata"),
    path("delete/<int:pk>/",views.deleteddata,name="deletedata"),
]