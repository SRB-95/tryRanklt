from .import views
from django.urls import path

app_name = 'rankltRight'
urlpatterns = [
    path('', views.user_form, name = 'user_form'),
    path('details/', views.details, name = 'details'),
    path('f_search/', views.f_search, name = 'f_search'),
    path('details/<user_id>', views.gi_ajax, name = 'gi_ajax'),
]