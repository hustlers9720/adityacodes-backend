# FastAPI Backend 

This is the backend service for the application built using FastAPI, SQLAlchemy, and JWT Authentication.

---

## Features

* User Authentication (Login / Register with JWT)
* Product Management (Add & Fetch Products)
* Checkout API
* Database Integration using SQLAlchemy
* CORS Enabled for frontend integration

---

## Tech Stack

* FastAPI
* Python
* SQLAlchemy
* SQLite (can be upgraded to PostgreSQL)
* JWT Authentication

---

## Project Structure

```
backend/
│── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── products.py
│   │   └── checkout.py
│   ├── core/
│   │   └── security.py
│   ├── db/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── seed.py
│   ├── schemas/
│   │   └── user.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <your-repo-url>
cd backend
```

---

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the Server (Local)

```
python -m uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

## API Endpoints

### Auth

* POST /api/v1/auth/register → Register user
* POST /api/v1/auth/login → Login user

---

### Products

* GET /api/v1/products/ → Get all products
* POST /api/v1/products/add → Add new product

---

### Checkout

* POST /api/v1/checkout/ → Checkout items

---

## Authentication

JWT token is returned on login/register.

Send token in headers:

```
Authorization: Bearer <token>
```

---

## Deployment

Run in production:

```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## Notes

* SQLite is used for development
* For production, use PostgreSQL
* Ensure CORS is properly configured

---

## Future Improvements

* Role-based authentication
* Image upload support
* Payment gateway integration
* Admin dashboard

---

## Author

Developed by Your Name

---

## Support

If you like this project, consider giving it a star on GitHub.
