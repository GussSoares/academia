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
from . import api, views

app_name = "usuario"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('usuario/', include())

    # USUARIOS
    url(r'^list-users/$', views.list_user, name="list_users"),
    url(r'^profile/$', views.user_profile, name="user_profile"),

    # APIS
    url(r'^api/get-usuario/(?P<pk>\d+)$', api.get_usuario, name="api_get_usuario"),
    url(r'^api/list-usuarios/$', api.list_usuarios, name="api_list_usuarios"),
    url(r'^api/list-usuario-ajax/$', api.list_usuario_ajax, name="list_usuario_ajax"),
    url(r'^api/edit-usuario-ajax/$', api.edit_usuario_ajax, name="edit_usuario_ajax"),
]
