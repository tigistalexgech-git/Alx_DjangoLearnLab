## Book API Views

### Endpoints

- GET /api/books/  
  Retrieves all books (public)

- GET /api/books/<id>/  
  Retrieves a single book (public)

- POST /api/books/create/  
  Creates a new book (authenticated users only)

- PUT /api/books/<id>/update/  
  Updates an existing book (authenticated users only)

- DELETE /api/books/<id>/delete/  
  Deletes a book (authenticated users only)

### Permissions
- Read-only access is public
- Create, update, delete require authentication
