from django.views.generic import TemplateView

from app1.models import About


def custom_about(request):
    context = {
        'about': About.objects.first()
    }
    return context
