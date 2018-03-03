from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^obtain-auth-token/$', obtain_auth_token)
]
