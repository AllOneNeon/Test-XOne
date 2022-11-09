from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crud.views import CategoryViewSet, TransactionViewSet

router = DefaultRouter()
router.register("", TransactionViewSet, basename="transaction")

router1 = DefaultRouter()
router1.register("", CategoryViewSet, basename="category")

urlpatterns = [
    path("transaction/", include(router.urls)),
    path("category/", include(router1.urls))
]

