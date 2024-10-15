from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import RealEstateListing, VehicleListing, VehiclePartListing
from .serializers import (
    RealEstateListingSerializer,
    VehicleListingSerializer,
    VehiclePartListingSerializer,
)


class RealEstateListingListView(generics.ListAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at"]


class RealEstateListingListCreateView(generics.ListCreateAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RealEstateListingUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RealEstateListing.objects.all()
    serializer_class = RealEstateListingSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


# ویوها برای وسایل نقلیه
class VehicleListingListView(generics.ListAPIView):
    queryset = VehicleListing.objects.all()
    serializer_class = VehicleListingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at"]


class VehicleListingListCreateView(generics.ListCreateAPIView):
    queryset = VehicleListing.objects.all()
    serializer_class = VehicleListingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VehicleListingUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehicleListing.objects.all()
    serializer_class = VehicleListingSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


# ویوها برای قطعات وسایل نقلیه
class VehiclePartListingListView(generics.ListAPIView):
    queryset = VehiclePartListing.objects.all()
    serializer_class = VehiclePartListingSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at"]


class VehiclePartListingListCreateView(generics.ListCreateAPIView):
    queryset = VehiclePartListing.objects.all()
    serializer_class = VehiclePartListingSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VehiclePartListingUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehiclePartListing.objects.all()
    serializer_class = VehiclePartListingSerializer

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
