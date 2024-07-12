from .models import Company


def site_info(request):
    site_info = Company.objects.last()
    return {'info':site_info}