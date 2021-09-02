"""demo URL Configuration

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
from django.urls import path, include
from django.views.generic import TemplateView

from demo import views


urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('oidc/', include('mozilla_django_oidc.urls')),
    path("product/create/", views.ProductCreateView.as_view(), name="product-create"),
    path("product/<int:pk>/change/", views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("switch-domain/<int:domain_id>/", views.SwitchDomainView.as_view(), name="switch-domain"),
]
