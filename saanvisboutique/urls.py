"""saanvisboutique URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/customer/', views.CustomerAPI.as_view()),
    path('api/customer/<int:pk>', views.CustomerAPI.as_view()),
    path('api/customer/create', views.CustomerAPI.as_view()),
    path('api/customer/delete/<int:pk>', views.CustomerAPI.as_view()),
    path('api/customer/update/<int:pk>', views.CustomerAPI.as_view()),

    path('api/vendor/', views.VendorAPI.as_view()),
    path('api/vendor/create', views.VendorAPI.as_view()),
    path('api/vendor/delete/<int:pk>', views.VendorAPI.as_view()),
    path('api/vendor/update/<int:pk>', views.VendorAPI.as_view()),

    path('api/customer/transaction/<int:pk>', views.CustomerTransactionAPI.as_view()),
    path('api/customer/transaction/create', views.CustomerTransactionAPI.as_view()),
    path('api/customer/transaction/delete/<int:pk>', views.CustomerTransactionAPI.as_view()),
    path('api/customer/transaction/update/<int:pk>', views.CustomerTransactionAPI.as_view()),

    path('api/product/update/<int:pk>', views.ProductAPI.as_view()),
    path('api/product/delete/<int:pk>', views.ProductAPI.as_view()),
]
