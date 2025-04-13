# Store Server

## Project Overview
This project is a Django-based web application designed to manage an online store. It includes functionality for user registration and authentication, product browsing, shopping cart management, and order processing. The project integrates Stripe for payment processing, features asynchronous tasks with Celery, and uses PostgreSQL as the database backend.
The store server also implements filtering, pagination, and the ability to send email verifications to users. It is optimized for testing and includes caching to improve performance. 

## Features
* User Authentication: Custom user registration and login, with email verification for new users.
* Product Management: Ability to browse, filter, and paginate products in the store.
* Shopping Cart: Add products to the cart, update quantities, and remove items.
* Order Management: Create orders, process payments with Stripe, and view order details.
* Email Verification: Send email verifications during registration.
* Admin Interface: Manage products, orders, and users through Django Admin.
* Testing: Comprehensive testing for views and user registration.
* Caching: Improve performance using caching techniques.
* Asynchronous Tasks: Handle background tasks using Celery.

## Technologies Used
* Django: Python web framework for building the application.
* Stripe: Payment gateway for processing orders.
* PostgreSQL: Relational database management system for data storage.
* Celery: Asynchronous task queue for handling background tasks.
* Redis: In-memory data store for caching.
* django-allauth: Third-party library for handling user authentication and OAuth.
* django-debug-toolbar: Tool for debugging and inspecting cache usage.
* Google SMTP: Email service for sending verification emails.
* Django REST Framework: For building Web APIs.
* Gunicorn: WSGI HTTP server for running the Django application in production.
