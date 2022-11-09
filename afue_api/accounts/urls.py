from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import DefaultRouter

from accounts.views import UserInfoViewSet, LoginView

router = DefaultRouter()
router.register("", UserInfoViewSet, basename="user-info")

urlpatterns = [
    path("user/", include(router.urls)),
    path("registr/", UserViewSet.as_view({"post": "create"}), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]