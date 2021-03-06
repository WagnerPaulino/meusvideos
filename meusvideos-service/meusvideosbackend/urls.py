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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
usuario_view_set = UsuarioViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
videos_view_set = VideoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
resenha_view_set = ResenhaViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path(r'dj-rest-auth/', include('dj_rest_auth.urls')),
    path(r'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'videos/<int:pk>/', VideoViewSet.as_view({'put': 'update'}), name="videos"),
    path(r'videos/', videos_view_set, name="videos"),
    path(r'usuarios/', usuario_view_set, name="usuarios"),
    path(r'resenhas/', resenha_view_set, name="resenhas"),
    path(r'', include(router.urls))
]
