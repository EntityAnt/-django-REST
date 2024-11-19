from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')


urlpatterns = [
    # path("", IndexView.as_view(), name="index"),
    # path("vehicles/", VehicleListView.as_view(), name="vehicles"),
    # path("detail/<int:pk>/", VehicleDetailView.as_view(), name="detail"),
] + router.urls
