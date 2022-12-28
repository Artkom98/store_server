from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='index'),
    path('basket-add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', views.basket_delete, name='basket_delete'),
]
