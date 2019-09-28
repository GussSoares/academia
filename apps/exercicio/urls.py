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
import academia.apps.exercicio.api as api

app_name = "exercicio"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('usuario/', include())
    url(r'^list-exercicios/$', api.list_exercicios, name="list_exercicios"),
    url(r'^create-exercicio/$', api.create_exercicio, name="create_exercicio"),
    url(r'^update-exercicio/(?P<pk>\d+)$', api.update_exercicio, name="update_exercicio"),
    url(r'^get-exercicio/(?P<pk>\d+)$', api.get_exercicio, name="get_exercicio"),

]
