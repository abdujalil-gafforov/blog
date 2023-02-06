import os
import django
import datetime
from app1.models import Post
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()


def cron_job():
    date = datetime.date.today()
    date_delta = datetime.timedelta(7)
    Post.objects.filter(Q(created_at__lt=date - date_delta), Q(status=Post.Status.CANCEL)).delete()

