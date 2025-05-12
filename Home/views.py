from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render
from django.views import View
from users.models import ProprietaireVE, Fournisseur
from stations.models import station, Reservation

# Fonction utilitaire pour formater les nombres (K, M)


def format_number(num):
    if num >= 1000000:
        return f"{num / 1000000:.1f}M+"
    elif num >= 1000:
        return f"{num / 1000:.1f}K+"
    else:
        return f"{num}+"

# Create your views here.


def Home(request, username):
    if ProprietaireVE.objects.filter(username=username).exists():
        user = ProprietaireVE.objects.get(username=username)
    if Fournisseur.objects.filter(username=username).exists():
        user = Fournisseur.objects.get(username=username)

    if user and (
        Fournisseur.objects.filter(
            username=username).exists() or ProprietaireVE.objects.filter(
            username=username).exists()):
        return Home_user_page.as_view()(request, user)
    else:
        return Home_admin_page.as_view()(request)


class Home_public_page(View):
    template_name = 'Home.html'

    def get(self, request):
        # Calculer les statistiques réelles
        stations_count = station.objects.count()

        # Compter les villes uniques (basé sur les adresses des stations)
        cities_count = station.objects.values('adresse').distinct().count()

        # Nombre d'utilisateurs (propriétaires de VE)
        users_count = ProprietaireVE.objects.count()

        # Nombre de recharges effectuées
        charges_count = Reservation.objects.count()

        # Formater les nombres
        stats = {
            'stations_count': format_number(stations_count),
            'cities_count': format_number(cities_count),
            'users_count': format_number(users_count),
            'charges_count': format_number(charges_count)
        }

        return render(request, self.template_name, context=stats)


class Home_user_page(View):
    template_name = 'Home.html'

    def get(self, request, user):
        # Calculer les statistiques réelles
        stations_count = station.objects.count()

        # Compter les villes uniques (basé sur les adresses des stations)
        cities_count = station.objects.values('adresse').distinct().count()

        # Nombre d'utilisateurs (propriétaires de VE)
        users_count = ProprietaireVE.objects.count()

        # Nombre de recharges effectuées
        charges_count = Reservation.objects.count()

        # Formater les nombres
        stats = {
            'stations_count': format_number(stations_count),
            'cities_count': format_number(cities_count),
            'users_count': format_number(users_count),
            'charges_count': format_number(charges_count),
            'user': user
        }

        return render(request, self.template_name, context=stats)


class Home_admin_page(View):
    template_name = 'Home_Admin.html'

    def get(self, request, user):
        return render(request, self.template_name, context={'user': user})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


# Ajouter ces nouvelles vues
# Ajoutez ces classes à la fin du fichier views.py
class PrivacyPolicyView(View):
    template_name = 'privacy_policy.html'

    def get(self, request):
        return render(request, self.template_name)


class TermsOfServiceView(View):
    template_name = 'terms_of_service.html'

    def get(self, request):
        return render(request, self.template_name)
