from django.urls import path
from . import views

urlpatterns = [
    #path("", views.current_time, name = "curret_time"),
    path("",views.index, name = 'index'),
    #path("add",views.add, name = 'add'),
    path("hours_ahead",views.hours_ahead, name="hours_ahead")
]
