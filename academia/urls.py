"""academia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
import academia.apps.usuario.urls as usuario
import academia.apps.exercicio.urls as exercicio
import academia.apps.api.urls as api
import academia.apps.dashboard.urls as dashboard
import academia.apps.acl.urls as acl

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('usuario/', include())
    # path('usuario/', include('apps.usuario.urls')),

    # DEFAULT
    url(r'^admin/', admin.site.urls),

    # ACL
    url(r'^acl/', include((acl, 'acl'), namespace="acl")),

    # DASHBOARD
    url(r'^$', dashboard.index, name="index"),

    # API
    url(r'^api/', include(api, namespace="api")),

    # USUARIO
    url(r'^usuario/', include(usuario, namespace="usuario")),

    # EXERCICIO
    url(r'^exercicio/', include(exercicio, namespace="exercicio")),
]
