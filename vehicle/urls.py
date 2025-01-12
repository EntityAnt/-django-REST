from django.urls import path
from rest_framework.routers import DefaultRouter

from vehicle.apps import VehicleConfig
from vehicle.views import (CarViewSet, MilageCreateAPIView, MilageListAPIView, MotoCreateAPIView, MotoDestroyAPIView,
                           MotoListAPIView, MotoMilageListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView)

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r"cars", CarViewSet, basename="cars")


urlpatterns = [
    path("moto/new/", MotoCreateAPIView.as_view(), name="moto-create"),
    path("moto/", MotoListAPIView.as_view(), name="moto-list"),
    path("moto/<int:pk>/", MotoRetrieveAPIView.as_view(), name="moto-get"),
    path("moto/edit/<int:pk>/", MotoUpdateAPIView.as_view(), name="moto-edit"),
    path("moto/delete/<int:pk>/", MotoDestroyAPIView.as_view(), name="moto-delete"),
    path("moto/milage/", MotoMilageListAPIView.as_view(), name="moto-milage"),
    # milage
    path("milage/new/", MilageCreateAPIView.as_view(), name="milage-create"),
    path("milage/", MilageListAPIView.as_view(), name="milage-list"),
] + router.urls
