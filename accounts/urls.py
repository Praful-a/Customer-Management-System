from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('createorder/<str:pk>/', views.createOrder, name='createorder'),
    path('update/<str:pk>/', views.updateorder, name='updateorder'),
    path('delete/<str:pk>/', views.deleteorder, name='deleteorder'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSettings, name='account')
]
