CAPSTONE PROJECT

PROJECT PLAN

Name:
Proactive_Management

Problem:
A Company has many customers it provides internet services to, during outages and planned activities, engineers will have to manually send emails to affected customers one by one. This has not been efficient because the same engineers are monitoring and resolving other customer complaints.

Solution:
Build a website where customer notification and engagements can be easily managed via emails.
Build a customer database to sort out customers names, locations, last mile site, service type etc.
Create various accounts for Engineer logins

FEATURES
The project will have these key features:
Customer Database: Build a central, searchable database to store and organize customer details like name, location, last-mile site, and service type. 
Engineer Accounts: Engineers will need a secure way to log in.Set up user accounts with proper authentication to ensure only authorized personnel can access and manage the system.
Notification Management: The core functionality will be to create, view, and manage notifications. Engineers can draft messages, and we'll save them in our database.
Targeted Email Sending: The system will allow engineers to select a group of customers (for example, by location or service type) and send them a single, mass email with the push of a button.
Future-Proofing: Lay the groundwork for future features, such as sending emails to customers at the start and end planned maintenance, and a post-outage "Root Cause Analysis" summary.

API 
The Project will be built on Django REST Framework (DRF).

Model & API Endpoints

Models
Customer: To store customer details like name, email, location, last_mile_site, and service_type.
Engineer: A custom user model for engineer logins and authentication.
Notification: To save the actual messages, linking them to a specific Engineer and the Customer list they are being sent to.
API Endpoints

ENDPOINTS
DESCRIPTION
POST /api/login/
Log in an engineer and get a token
GET, POST /api/customers/
Get a list of customers or create a new one
GET, PUT, DELETE /api/customers/<id>/
View, update, or delete a specific customer
GET, POST /api/notifications/
Get a list of notifications or create a new one
GET, PUT, DELETE /api/notifications/<id>/
View, update, or delete a specific notification
POST /api/notifications/send/
Take a notification ID and a list of customer IDs to send emails to


