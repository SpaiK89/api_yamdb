from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router_v1 = DefaultRouter()
# router_v1.register('categories', views.CategoryViewSet, basename='categories')
# router_v1.register('genres', views.GenreViewSet, basename='genres')
# router_v1.register('titles', views.GenreViewSet, basename='titles')
router_v1.register('users', views.UserViewSet, basename='users')

authentication = [
    path("signup/", views.get_signup),
    path("token/", views.get_token),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path("v1/auth/", include(authentication)),
]
