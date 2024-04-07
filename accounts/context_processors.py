from .models import LogoImage


def get_logo(request):
    try:
        obj = LogoImage.objects.first()
        if obj:
            logo = obj.image
        else:
            logo = ""
        return {
            'logo': logo,
            }
    except LogoImage.DoesNotExist:
        return {
            'logo': "",
            }
