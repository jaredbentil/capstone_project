# Social Media API

This repository contains the foundational setup for a Social Media API built with Django and Django REST Framework. It includes a custom user model, token-based authentication, and endpoints for user registration, login, and profile management.

## Features

-   **Custom User Model**: Extends Django's `AbstractUser` with fields for `bio`, `profile_picture`, and a `followers` system.
-   **Token Authentication**: Uses Django REST Framework's `authtoken` for secure, token-based authentication.
-   **Core API Endpoints**:
    -   User Registration (`/api/accounts/register/`)
    -   User Login (`/api/accounts/login/`)
    -   User Profile Management (`/api/accounts/profile/`)

## Project Setup

Follow these steps to get the project running locally.

### Prerequisites

-   Python 3.8+
-   pip (Python package installer)
-   Virtualenv (recommended)

(All endpoints require authentication: Authorization: Token <your_token>)