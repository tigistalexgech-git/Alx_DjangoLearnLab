# Introduction to Django

This project demonstrates the basic setup of a Django development environment.

## Project Name
LibraryProject

## Objectives
- Install Django
- Create a Django project
- Run the Django development server
- Understand Django project structure

# Permissions & Groups Setup

**Custom Permissions for Article Model:**
- can_view
- can_create
- can_edit
- can_delete

**Groups:**
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → can_view, can_create, can_edit, can_delete

**Usage in Views:**
Use `@permission_required('bookshelf.can_edit', raise_exception=True)` to protect views.

**Notes:**
- Always assign users to a group or give individual permissions.
- Permissions are automatically available in the admin site.
