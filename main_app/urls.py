"""main_app URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from factory.views import ConsumerView, ConsumerDetailView, ProductListView, ProductDetailView
from user.views import UserView, UserDetailView, OrderView, OrderDetailView
from delivery.views import DeliveryServiceView, DeliveryServiceDetailView, DeliveryManView, DeliveryManDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('factory/', ConsumerView.as_view()),
    path('factory/<int:pk>/', ConsumerDetailView.as_view()),
    path('order/', OrderView.as_view()),
    path('order/<int:pk>/', OrderDetailView.as_view()),
    path('delivery_man/', DeliveryManView.as_view()),
    path('delivery_man/<int:pk>/', DeliveryManDetailView.as_view()),
    path('deliver_service/', DeliveryServiceView.as_view()),
    path('deliver_service/<int:pk>/', DeliveryServiceDetailView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
