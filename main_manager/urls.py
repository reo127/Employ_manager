"""employ_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employs/<int:employ_sno>', views.employs, name='employs'),
    path('employsEadit/<str:employ_name>', views.Eaditemploys, name='employs'),
    path('employsUpdate/<str:employ_name>', views.UpdateEmploys, name='UpdateEmploys'),
    path('employsDel/<int:employ_sno>', views.employsDel, name='employsDel'),
    path('addemploys', views.AddEmploys, name='addemploys'),
]
