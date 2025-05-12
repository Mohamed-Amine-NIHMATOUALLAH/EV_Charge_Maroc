# EV_Charge_Maroc

## Description
EV_Charge_Maroc est une plateforme Django complète pour gérer les stations de recharge pour véhicules électriques au Maroc. Le projet permet aux utilisateurs de trouver des stations de recharge sur une carte interactive, réserver des sessions de charge, effectuer des paiements via Stripe, et générer des QR codes pour l'authentification.

## Fonctionnalités principales
- 🔌 Localisation des stations de recharge sur carte
- 📅 Système de réservation de sessions de charge
- 💳 Intégration de paiements via Stripe
- 📱 Génération de QR codes pour l'authentification
- 👤 Gestion des profils utilisateurs
- 📊 Tableau de bord administrateur

## Prérequis
- Python 3.13.2
- XAMPP (pour MySQL/MariaDB)
- Git
- Compte Stripe (pour les tests de paiement)

## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/Mohamed-Amine-NIHMATOUALLAH/EV_Charge_Maroc.git
cd EV_Charge_Maroc
```

### 2. Créer et activer l'environnement virtuel
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt

# Assurez-vous d'installer python-dotenv s'il n'est pas dans requirements.txt
pip install python-dotenv
```

### 4. Configurer les variables d'environnement
```bash
# Copier le fichier template
cp .env.template .env

# Modifier le fichier .env avec vos informations
```

⚠️ **IMPORTANT** : 
- Le fichier `.env` doit être créé à la racine du projet (dans le même dossier que `manage.py`)
- Ce fichier contient des informations sensibles et n'est PAS inclus dans le dépôt Git
- Vous devez créer votre propre fichier `.env` à partir du template et y ajouter vos propres valeurs pour :

  - **Django** : Générez une nouvelle SECRET_KEY pour la sécurité
  - **Base de données** : Configurez selon votre installation MySQL
  - **Stripe** : Ajoutez vos propres clés API Stripe pour les tests de paiement
  - **Email** : Configurez avec vos propres identifiants SMTP

Pour générer une nouvelle Django SECRET_KEY, vous pouvez utiliser cette commande :
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Configurer la base de données
- Démarrer XAMPP et activer MySQL
- Créer une base de données nommée `ev_charge_maroc`

### 6. Appliquer les migrations
```bash
python manage.py migrate
```

### 7. Importer les données de stations (optionnel)
```bash
python manage.py shell
exec(open('import_openchargemap.py').read())
```

### 8. Lancer le serveur de développement
```bash
python manage.py runserver
```

## Structure du projet
```
EV_Charge_Maroc/
├── EV_Charge_Maroc/      # Projet principal Django
├── Home/                 # Application page d'accueil
├── help/                 # Application d'aide
├── map/                  # Application de carte
├── payments/             # Application de paiements
├── stations/             # Application de gestion des stations
├── users/                # Application de gestion des utilisateurs
├── static/               # Fichiers statiques (CSS, JS, images)
├── media/                # Fichiers téléchargés par les utilisateurs
├── templates/            # Templates HTML
├── manage.py             # Script de gestion Django
└── requirements.txt      # Dépendances du projet
```

## Résolution des problèmes courants

### Problèmes de configuration
1. **Erreur "No module named 'dotenv'"** 
   - Solution : Installez python-dotenv avec `pip install python-dotenv`

2. **Erreur de connexion à la base de données**
   - Vérifiez que XAMPP est en cours d'exécution
   - Assurez-vous que les informations de connexion dans `.env` sont correctes
   - Vérifiez que la base de données `ev_charge_maroc` existe

3. **Erreur avec les variables d'environnement**
   - Vérifiez que vous avez bien créé le fichier `.env` à partir du template
   - Assurez-vous que le fichier est placé à la racine du projet
   - Redémarrez le serveur Django après modification du fichier `.env`

4. **Problèmes avec Stripe**
   - Assurez-vous d'avoir créé un compte Stripe et d'avoir ajouté vos clés d'API dans le fichier `.env`
   - Pour les tests, utilisez les numéros de cartes de test fournis par Stripe

5. **Erreurs d'envoi d'emails**
   - Si vous utilisez Gmail, assurez-vous d'avoir activé "l'accès des applications moins sécurisées" ou de générer un mot de passe d'application

## Contact et licence
Projet développé par Mohamed Amine Nihmatouallah.

Pour toute question ou demande d'autorisation, veuillez me contacter à [mohamed.amine.nihmatouallah@gmail.com](mailto:mohamed.amine.nihmatouallah@gmail.com).

**Avertissement :**  
Ce projet est protégé par des droits d'auteur. Il est strictement interdit d'utiliser, de modifier ou de distribuer ce code sans l'autorisation explicite de l'auteur.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](./LICENSE) pour plus d'informations.