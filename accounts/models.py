from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    bio = models.TextField(blank=True, null=True, verbose_name="بیوگرافی")
    location = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="موقعیت"
    )
    profile_picture = models.ImageField(
        upload_to="profiles/", blank=True, null=True, verbose_name="عکس پروفایل"
    )

    def __str__(self):
        return f"پروفایل {self.user.username}"

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل‌ها"
