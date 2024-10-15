import django_filters
from .models import Listing, Category


class ListingFilter(django_filters.FilterSet):
    # فیلتر بازه‌ای برای قیمت
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    # فیلتر بازه‌ای برای سال ساخت
    min_year = django_filters.NumberFilter(field_name="year_built", lookup_expr="gte")
    max_year = django_filters.NumberFilter(field_name="year_built", lookup_expr="lte")

    # فیلتر برای جستجوی نسبی بر اساس عنوان
    title_contains = django_filters.CharFilter(
        field_name="title", lookup_expr="icontains"
    )

    # فیلتر بر اساس دسته‌بندی والد (برای زیر دسته‌بندی‌ها)
    parent_category = django_filters.ModelChoiceFilter(
        field_name="category__parent", queryset=Category.objects.all()
    )

    class Meta:
        model = Listing
        fields = [
            "category",
            "location",
            "min_price",
            "max_price",
            "min_year",
            "max_year",
            "title_contains",
        ]
