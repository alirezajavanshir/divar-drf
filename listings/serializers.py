from rest_framework import serializers
from .models import RealEstateListing, VehicleListing, VehiclePartListing


class RealEstateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateListing
        fields = "__all__"


class VehicleListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleListing
        fields = "__all__"


class VehiclePartListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePartListing
        fields = "__all__"
