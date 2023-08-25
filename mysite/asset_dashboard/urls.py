from django.urls import path
from .views import *
from . import views


urlpatterns=[
    path("",views.dashboardpage, name="dashboardpage"),
    path("/layout-static",views.layoutpage, name="layoutpage"),
    path("/layout-sidenav-light",views.light, name="light"),
    path("/charts",views.chart, name="chart"),
    path("/tables",views.table, name="table"),
]