from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns =[
    path('', views.product_list_create_view, name='product_list_create_view')
]