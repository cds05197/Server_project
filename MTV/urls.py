from django.urls import path
from . import views

app_name='MTV'
urlpatterns = [
    path('',views.Main),
    path('mycar/', views.Mycar, name="mycar"),
    path('login/',views.Login, name="login"),
    path('main/',views.Main, name="main"),
    path('session_timeout/',views.Timeout),
    path('make/', views.Create),
    path('makeopta/', views.Create_Opta),
    path('makeoptb/', views.Create_Optb),
    path('makeoptc/', views.Create_Optc),
    path('makeoptd/', views.Create_Optd),
    path('delete/', views.Delete),
    path('search/', views.Search, name="search"),
    path('search/<keyword>/', views.Search_reset, name="search_reset"),
    path('<int:Car_id>/',views.Detail, name="Detail"),
    path('<man>/', views.Sort_Main, name="Sort_Main"),
    path('search/<man>/<keyword>/', views.Sort_Search, name="Sort_Search"),
    path('create/<car>/', views.Mycar_Create, name="mycar_create"),
    path('delete/<car>/', views.Mycar_Delete, name="mycar_delete"),
    
]
