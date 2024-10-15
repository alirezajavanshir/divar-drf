from django.db import models


# مدل انتزاعی برای مشخصات مشترک
class AbstractListing(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    location = models.CharField(max_length=255, verbose_name="موقعیت")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت")
    image = models.ImageField(upload_to="images/", verbose_name="تصویر")

    class Meta:
        abstract = True
        verbose_name = "آگهی انتزاعی"
        verbose_name_plural = "آگهی‌های انتزاعی"


# مدل املاک
class RealEstateListing(AbstractListing):
    area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="متراژ")
    year_built = models.IntegerField(verbose_name="سال ساخت")
    floor = models.IntegerField(verbose_name="طبقه")
    parking = models.BooleanField(default=False, verbose_name="پارکینگ")
    elevator = models.BooleanField(default=False, verbose_name="آسانسور")
    storage = models.BooleanField(default=False, verbose_name="انباری")

    class Meta:
        verbose_name = "آگهی املاک"
        verbose_name_plural = "آگهی‌های املاک"


# مدل وسایل نقلیه
class VehicleListing(AbstractListing):
    vehicle_type = models.CharField(
        max_length=50,
        choices=[("car", "خودرو"), ("motorcycle", "موتورسیکلت"), ("truck", "کامیون")],
        verbose_name="نوع وسیله نقلیه",
    )
    model = models.CharField(max_length=100, verbose_name="مدل")
    color = models.CharField(max_length=50, verbose_name="رنگ")
    mileage = models.IntegerField(verbose_name="کارکرد")
    fuel_type = models.CharField(max_length=50, verbose_name="نوع سوخت")

    class Meta:
        verbose_name = "آگهی وسیله نقلیه"
        verbose_name_plural = "آگهی‌های وسایل نقلیه"


# مدل قطعات وسایل نقلیه
class VehiclePartListing(AbstractListing):
    class Meta:
        verbose_name = "آگهی قطعات وسایل نقلیه"
        verbose_name_plural = "آگهی‌های قطعات وسایل نقلیه"


# مدل‌های دسته‌بندی
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    parent = models.ForeignKey(
        "self",
        related_name="subcategories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="دسته‌بندی والد",
    )

    def __str__(self):
        return self.name

    def get_subcategories(self):
        return self.subcategories.all()

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
