# Django REST Framework: Book API

## Overview
This project demonstrates how to build a REST API using Django REST Framework (DRF) with generic views.

## API Endpoints

| Endpoint | Method | Description | Auth Required |
|----------|--------|------------|--------------|
| `/api/books/` | GET | List all books | No |
| `/api/books/` | POST | Add a new book | Yes |
| `/api/books/<id>/` | GET | Retrieve a single book | No |
| `/api/books/<id>/` | PUT | Update a book | Yes |
| `/api/books/<id>/` | DELETE | Delete a book | Yes |

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
