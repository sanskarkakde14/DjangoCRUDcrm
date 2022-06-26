from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/',views.loginPage,name="login"),
    path('loginout/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('products/',views.products,name="products"),
    path('customer/<str:pk_test>/',views.customer,name="customers"),
    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    path('update_order/<str:pk>',views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>',views.deleteOrder,name="delete_order"),
    path('account/',views.accountsettings,name="account"),

]

