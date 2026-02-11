# NofinishlineNrb Django Backend

## Features
- User registration, login, and profile
- JWT authentication
- Donations (create, list)
- Sponsors (create, list, update status)
- Role-based access (user/admin)
- File upload support (public/uploads)
- Email service (Nodemailer equivalent via Django email)
- Environment variable support via django-environ
- Error handling middleware

## Apps
- users
- donations
- sponsors
- common (shared utilities)

## Setup
1. Create a virtual environment and activate it
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set environment variables
4. Run migrations: `python manage.py migrate`
5. Run server: `python manage.py runserver`

## Main Routes
- POST /api/users/register
- POST /api/users/login
- GET /api/users/me
- POST /api/donations
- GET /api/donations
- POST /api/sponsors
- GET /api/sponsors
- PUT /api/sponsors/:id/status

## Notes
- Payment integration is mocked.
- Admin panel is default Django admin.
- See code for additional models and features.
