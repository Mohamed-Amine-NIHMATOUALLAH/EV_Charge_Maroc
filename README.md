# EV_Charge_Maroc

## Table of Contents

- [Description](#description)
- [Main Features](#main-features)
- [Prerequisites](#prerequisites)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Common Issues](#common-issues)
- [Contact](#contact)
- [License](#license)

## Description

EV_Charge_Maroc is a comprehensive Django platform for managing electric vehicle charging stations in Morocco. The project allows users to find charging stations on an interactive map, book charging sessions, make payments via Stripe, and generate QR codes for authentication.

## Main Features

- 🔌 Interactive map with charging station locations
- 📅 Charging session reservation system
- 💳 Stripe payment integration
- 📱 QR code generation for authentication
- 👤 User profile management
- 📊 Administrator dashboard

## Prerequisites

- Python 3.13.2
- XAMPP (for MySQL/MariaDB)
- Git
- Stripe account (for payment testing)

## Technologies Used

- **Django**: Backend framework for building the web application
- **Stripe**: For payment integration
- **OpenChargeMap API**: For importing station data
- **MySQL/MariaDB**: Database for storing application data
- **Python-dotenv**: For managing environment variables
- **HTML/CSS/JavaScript**: For the frontend

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mohamed-Amine-NIHMATOUALLAH/EV_Charge_Maroc.git
cd EV_Charge_Maroc
```

### 2. Create and Activate Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

# Make sure to install python-dotenv if it's not in requirements.txt
pip install python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file at the root of the project (same folder as `manage.py`) and add the following variables:

```plaintext
SECRET_KEY=your_django_secret_key
DATABASE_NAME=ev_charge_maroc
DATABASE_USER=root
DATABASE_PASSWORD=your_password
STRIPE_API_KEY=your_stripe_api_key
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_email_password
```

⚠️ **IMPORTANT**:

- The `.env` file contains sensitive information and is NOT included in the Git repository
- You must create your own `.env` file using the template above and add your own values for:
  - **Django**: Generate a new SECRET_KEY for security
  - **Database**: Configure according to your MySQL installation
  - **Stripe**: Add your own Stripe API keys for payment testing
  - **Email**: Configure with your own SMTP credentials

To generate a new Django SECRET_KEY, you can use this command:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Configure the Database

- Start XAMPP and activate MySQL
- Create a database named `ev_charge_maroc`

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Import Station Data (Optional)

```bash
python manage.py shell
exec(open('import_openchargemap.py').read())
```

### 8. Start the Development Server

```bash
python manage.py runserver
```

## QR Code Authentication Flow

The application uses QR codes for seamless authentication at charging stations:

1. Users book a charging session through the platform
2. A unique QR code is generated for the reservation
3. At the charging station, users scan this QR code to authenticate
4. The system validates the QR code and activates the charging session

## OpenChargeMap API Setup

To use the OpenChargeMap API for importing station data:

1. Register for an API key at [OpenChargeMap](https://openchargemap.org/site/developerinfo)
2. Add your API key to the `.env` file:
   ```
   OCM_API_KEY=your_openchargemap_api_key
   ```

## Project Structure

```
EV_Charge_Maroc/
├── EV_Charge_Maroc/      # Main Django project
├── Home/                 # Home page application
├── help/                 # Help application
├── map/                  # Map application
├── payments/             # Payments application
├── stations/             # Stations management application
├── users/                # User management application
├── static/               # Static files (CSS, JS, images)
├── media/                # User-uploaded files
├── templates/            # HTML templates
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Common Issues

### Configuration Problems

1. **Error "No module named 'dotenv'"**
   - Solution: Install python-dotenv with `pip install python-dotenv`

2. **Database Connection Error**
   - Verify that XAMPP is running
   - Ensure connection information in `.env` is correct
   - Check that the `ev_charge_maroc` database exists

3. **Environment Variable Errors**
   - Verify that you created the `.env` file from the template
   - Make sure the file is placed at the project root
   - Restart the Django server after modifying the `.env` file

4. **Issues with Stripe**
   - Make sure you've created a Stripe account and added your API keys to the `.env` file
   - For testing, use the test card numbers provided by Stripe

5. **Email Sending Errors**
   - If using Gmail, make sure you've enabled "less secure app access" or generated an application password

## Contact

Project developed by Mohamed Amine Nihmatouallah.

For questions or permission requests:
- Email: [mohamed.amine.nihmatouallah@gmail.com](mailto:mohamed.amine.nihmatouallah@gmail.com)
- LinkedIn: [Mohamed Amine NIHMATOUALLAH](https://www.linkedin.com/in/mohamed-amine-nihmatouallah/)

## License

This project is protected by copyright. Any use, modification, or distribution of this code is strictly prohibited without explicit permission from the author.  
The code may only be used for personal testing, educational purposes, or evaluation.

For permission requests, contact [mohamed.amine.nihmatouallah@gmail.com](mailto:mohamed.amine.nihmatouallah@gmail.com).