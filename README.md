# EasyStay (E_Booking)

[![Django](https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Next.js](https://img.shields.io/badge/Next.js-15.1-black?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![DRF](https://img.shields.io/badge/DRF-SimpleJWT-red?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![Swagger](https://img.shields.io/badge/OpenAPI-Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)](https://swagger.io/)

EasyStay is a full-stack rental property and booking platform built with Next.js 15 (React 19) and Django REST Framework. It provides end-to-end rental management with dedicated portals for Customers, Property Owners, and Platform Administrators.

---

## Why It Stands Out

- **Verification-First Moderation**: Property owners must provide utility bill verification alongside listing photos. Listings remain in a pending state until vetted and approved by an administrator, preventing fraudulent postings.
- **Multi-Role Custom Architecture**: Instead of generic user accounts, the system enforces strict model-level role separation (`Customer`, `Owner`, `Admin`) with customized dashboards, action permissions, and workflows.
- **Secure Cookie-Based JWT Sessions**: Combines stateless SimpleJWT tokens with HTTP-only secure cookie storage, eliminating XSS vulnerabilities while allowing seamless Next.js Edge Middleware route guarding.
- **Modern Full-Stack Synergy**: Leverages Next.js 15 Server Actions on the frontend for reactive UI mutations and Django 5.1 with OpenAPI 3 (drf-spectacular) on the backend for typed, fully documented endpoints.

---

## Core Features

- **Customers**: Search and filter verified properties, view multi-image galleries, schedule booking dates, review stay history, and make payments.
- **Owners**: Publish listings, upload rental images and proof of utility bills, track booking inquiries, and manage reservation approvals.
- **Administrators**: Moderation portal to review and accept/reject property submissions, manage user accounts, and audit platform activity.

---

## Tech Stack

- **Frontend**: Next.js 15, React 19, Lucide React, CSS Modules
- **Backend**: Python 3.12, Django 5.1, Django REST Framework, SimpleJWT, drf-spectacular, Pillow
- **Database**: MySQL / PostgreSQL / SQLite
- **API Documentation**: OpenAPI 3, Swagger UI, ReDoc

---

## Project Structure

```
EasyStay/
├── backend/                  # Django REST API
│   ├── backend/              # Core project config (settings, urls, wsgi)
│   ├── e_booking_api/        # API app (models, views, serializers, urls)
│   └── manage.py
├── frontend/                 # Next.js 15 web client
│   ├── src/
│   │   ├── actions/          # Next.js Server Actions
│   │   ├── app/              # App Router pages (auth, eazystay, protected)
│   │   ├── components/       # Reusable UI components
│   │   ├── libs/             # API client and fetch utilities
│   │   └── middleware.js     # Route protection & role redirection
│   └── package.json
├── media/                    # Property and verification uploads
└── requirements.txt          # Python dependencies
```

---

## Quickstart Guide

### 1. Backend Setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
```

Create `backend/.env`:
```env
ENVIRONMENT=development
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_NAME=easystay_db
DATABASE_USER=root
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

Apply migrations and start the server:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend runs at `http://localhost:8000`.

### 2. Frontend Setup

```bash
cd ../frontend
npm install
```

Create `frontend/.env.local`:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
```

Start development server:
```bash
npm run dev
```

Frontend runs at `http://localhost:3000`.

---

## Key URLs & API Endpoints

### URLs
- **Web App**: `http://localhost:3000`
- **Swagger Docs**: `http://localhost:8000/api/docs/`
- **ReDoc**: `http://localhost:8000/api/redoc/`
- **Django Admin**: `http://localhost:8000/admin/`

### Primary Endpoints
| Endpoint | Method | Role / Description |
|---|---|---|
| `/api/login/` | `POST` | Authenticate and obtain JWT tokens + role |
| `/api/customers/` | `POST` | Customer registration |
| `/api/owners/` | `POST` | Owner registration |
| `/api/rentallistings/` | `GET`, `POST` | Browse or publish property listings |
| `/api/rental-images/upload/` | `POST` | Upload property photos |
| `/api/utility-bill-images/upload/` | `POST` | Upload verification utility bills |
| `/api/bookings/` | `GET`, `POST`, `PATCH` | Create and manage reservations |
| `/api/payments/` | `GET`, `POST` | Record and view transactions |

