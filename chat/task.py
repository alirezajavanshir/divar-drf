# tasks.py

from celery import shared_task
from django.utils import timezone
from .models import ChatMessage


@shared_task
def delete_old_chat_messages():
    # تاریخ ۵ روز قبل را محاسبه کنید
    cutoff_date = timezone.now() - timezone.timedelta(days=5)
    # پیام‌های قدیمی‌تر از ۵ روز را حذف کنید
    ChatMessage.objects.filter(timestamp__lt=cutoff_date).delete()
