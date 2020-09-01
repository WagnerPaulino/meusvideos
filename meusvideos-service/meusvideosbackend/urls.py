"""meusvideosbackend URL Configuration

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
from django.urls import include, path
from rest_framework import routers
from meusvideosbackend.meusvideos.views import UsuarioViewSet, VideoViewSet, ResenhaViewSet

router = routers.DefaultRouter()
usuario_view_set = UsuarioViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
videos_view_set = VideoViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update'
})
resenha_view_set = ResenhaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path(r'videos/', videos_view_set, name="videos"),
    path(r'usuarios/', usuario_view_set, name="usuarios"),
    path(r'resenhas/', resenha_view_set, name="resenhas"),
]
