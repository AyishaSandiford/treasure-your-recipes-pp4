"""recipes_app URL Configuration

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
from recipes import views as index_views
from recipes import views as about_views
from recipes import views as contact_views
from dashboard import views as profile_views
from dashboard import views as dashboard_views

urlpatterns = [
    path('', index_views.index, name='index'),
    path('about/', about_views.about, name='about'),
    path('contact/', contact_views.contact, name='contact'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile_views.profile, name='profile'),
    path('accounts/dashboard/', dashboard_views.dashboard, name='dashboard')
]
