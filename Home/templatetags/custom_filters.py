from django import template
from users.models import Fournisseur, ProprietaireVE

register = template.Library()


@register.filter
def is_instance_of(user, class_path):
    if not user.is_authenticated:
        return False

    try:
        if class_path == "users.models.Fournisseur":
            return Fournisseur.objects.filter(id=user.id).exists()
        elif class_path == "users.models.ProprietaireVE":
            return ProprietaireVE.objects.filter(id=user.id).exists()
        return False
    except Exception:
        return False
