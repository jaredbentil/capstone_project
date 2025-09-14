# Permissions and Groups Setup

This application uses Django's built-in permissions and groups system to manage user access.

## Permissions

Custom permissions have been added to the `Book` model to control user actions:
- `bookshelf.can_view`: Allows a user to view books.
- `bookshelf.can_create`: Allows a user to create new books.
- `bookshelf.can_edit`: Allows a user to edit existing books.
- `bookshelf.can_delete`: Allows a user to delete books.

## Groups

Three groups have been created in the Django admin site and assigned specific permissions:
- **Admins:** Have all four permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).
- **Editors:** Have `can_view`, `can_create`, and `can_edit` permissions.
- **Viewers:** Have only the `can_view` permission.

## Enforcing Permissions

Views that handle book creation, editing, and deletion are protected by the `@permission_required` decorator, which ensures that only users with the correct permissions can perform these actions.
