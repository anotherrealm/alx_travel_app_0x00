# Travel Booking Platform (alx_travel_app_0x00)

## Overview
This backend system supports a travel booking platform for managing users (guests and hosts), properties, bookings, reviews, and payments. Built with **Django** and **Django REST Framework**.

## Features
- **User Management**: Differentiates between guests and hosts.
- **Properties**: Hosts can list their properties.
- **Bookings**: Guests can book properties.
- **Reviews**: Guests can leave property reviews.
- **Payments**: Tracks payments for bookings.

## Requirements
- Python 3.8+
- Django 3.2+
- Django REST Framework

## Installation

1. Clone the repo:


2. Set up a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Migrate the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

## Models

- **User**: Extends `AbstractUser` with `user_type` (guest/host).
- **Property**: Represents listed properties with details like price and availability.
- **Booking**: Tracks guest bookings for properties.
- **Review**: Allows guests to leave reviews for properties.
- **Payment**: Records payments associated with bookings.

## API Endpoints

- **/api/properties/**: List properties.
- **/api/bookings/**: List bookings.
- **/api/reviews/**: List reviews.
- **/api/payments/**: List payments.

## Seeding the Database

Run the seed command to populate the database with sample data:

```bash
python manage.py seed
