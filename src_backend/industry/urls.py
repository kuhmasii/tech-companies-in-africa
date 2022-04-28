from django.urls import path
from . import views


app_name = 'industry'

urlpatterns = [
    path('', views.tech_list, name='tech_list'),
    path('company/<str:alpha_name>/', views.tech_alphabeth, name='tech_alphabeth'),
    # path('company/industry/<str:indus_slug>/',views.tech_industry, name='tech_industry'),

]
