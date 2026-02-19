# Advanced Django REST Framework API Project

## Project Overview

This project is part of the **ALX Advanced API Development** curriculum.  
It demonstrates how to build a robust RESTful API using **Django** and **Django REST Framework (DRF)**, including:

- Custom serializers with validation
- Nested relationships
- Generic class-based views
- Permissions and authentication
- Filtering, searching, and ordering
- Comprehensive unit tests

---

## Technologies Used

- Python 3.11
- Django
- Django REST Framework
- django-filter
- SQLite (default database)

---



---

## Models

### Author
- `name` (CharField)

### Book
- `title` (CharField)
- `publication_year` (IntegerField)
- `author` (ForeignKey → Author)

**Relationship:**  
One Author → Many Books (one-to-many)

---

## Serializers

- **BookSerializer**
  - Serializes all Book fields
  - Includes custom validation to prevent future publication years

- **AuthorSerializer**
  - Serializes author name
  - Includes nested books using `BookSerializer`

---

## API Views

The project uses **generic class-based views**:

| Endpoint | Method | Description | Permission |
|--------|--------|------------|------------|
| `/api/books/` | GET | List all books | Public |
| `/api/books/<id>/` | GET | Retrieve a book | Public |
| `/api/books/create/` | POST | Create a book | Authenticated |
| `/api/books/<id>/update/` | PUT | Update a book | Authenticated |
| `/api/books/<id>/delete/` | DELETE | Delete a book | Authenticated |

---

## Permissions

- **Read operations** (List & Detail): Open to all users
- **Write operations** (Create, Update, Delete): Restricted to authenticated users using `IsAuthenticated`

---

## Filtering, Searching, and Ordering

The Book list endpoint supports:

### Filtering