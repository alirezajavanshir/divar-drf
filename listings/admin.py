from django.contrib import admin
from .models import RealEstateListing, VehicleListing, VehiclePartListing, Category


@admin.register(RealEstateListing)
class RealEstateListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "location",
    )  # و دیگر فیلدهای مورد نظر
    search_fields = ("title", "description")


@admin.register(VehicleListing)
class VehicleListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "price",
        "vehicle_type",
        "model",
    )  # و دیگر فیلدهای مورد نظر
    search_fields = ("title", "description")


@admin.register(VehiclePartListing)
class VehiclePartListingAdmin(admin.ModelAdmin):
    list_display = ("price",)  # و دیگر فیلدهای مورد نظر
    search_fields = ("part_name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")  # و دیگر فیلدهای مورد نظر
