from django.urls import path
from .views import (
    RealEstateListingListView,
    RealEstateListingListCreateView,
    RealEstateListingUpdateDeleteView,
    VehicleListingListView,
    VehicleListingListCreateView,
    VehicleListingUpdateDeleteView,
    VehiclePartListingListView,
    VehiclePartListingListCreateView,
    VehiclePartListingUpdateDeleteView,
)

urlpatterns = [
    path("real-estate/", RealEstateListingListView.as_view(), name="real-estate-list"),
    path(
        "real-estate/create/",
        RealEstateListingListCreateView.as_view(),
        name="real-estate-create",
    ),
    path(
        "real-estate/<int:pk>/",
        RealEstateListingUpdateDeleteView.as_view(),
        name="real-estate-update-delete",
    ),
    path("vehicles/", VehicleListingListView.as_view(), name="vehicle-list"),
    path(
        "vehicles/create/",
        VehicleListingListCreateView.as_view(),
        name="vehicle-create",
    ),
    path(
        "vehicles/<int:pk>/",
        VehicleListingUpdateDeleteView.as_view(),
        name="vehicle-update-delete",
    ),
    path(
        "vehicle-parts/", VehiclePartListingListView.as_view(), name="vehicle-part-list"
    ),
    path(
        "vehicle-parts/create/",
        VehiclePartListingListCreateView.as_view(),
        name="vehicle-part-create",
    ),
    path(
        "vehicle-parts/<int:pk>/",
        VehiclePartListingUpdateDeleteView.as_view(),
        name="vehicle-part-update-delete",
    ),
]
