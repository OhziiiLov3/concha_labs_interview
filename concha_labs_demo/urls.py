"""concha_labs_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path 
from main_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name="home"),
    # TEST ROUTES
    path('accounts/', views.useraccount_list, name='accounts'),
    path('accounts/<int:id>', views.useraccount_detail),
    # USER ACCOUNT CRUD
    path('useraccount', views.useraccount, name='useraccount'),
    path('show', views.show, name='show'),
    path('search_accounts', views.search_accounts, name='search_accounts'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    # AUDIO CRUD
    path('audio', views.audio, name='audio'),
    path('show/audio', views. audio_show),
]
