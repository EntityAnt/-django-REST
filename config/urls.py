from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("vehicle.urls", namespace="vehicle")),
    path("users/", include("users.urls", namespace="users")),
]
