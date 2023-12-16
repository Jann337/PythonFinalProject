"""radicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('invoices/', include('invoices.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('sales/', include('sales.urls')),
    path('settings/', include('settings.urls')),
    path('about_page/', include('about_page.urls')),
    path('account_page/', include('account_page.urls')),
    path('home_page/', include('home_page.urls')),
    path('products_page/', include('products_page.urls')),
    path('services_page/', include('services_page.urls')),
    path('shopping_cart_page/', include('shopping_cart_page.urls')),
]
