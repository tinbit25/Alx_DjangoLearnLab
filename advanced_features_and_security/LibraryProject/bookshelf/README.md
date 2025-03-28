# Managing Permissions and Groups

## Overview
This Django project implements a system of permissions and groups to control access to different parts of the application. Custom permissions such as `can_view`, `can_create`, `can_edit`, and `can_delete` are used to restrict access to model instances based on user roles.

## Permissions
- `can_view`: Permission to view model instances.
- `can_create`: Permission to create new model instances.
- `can_edit`: Permission to edit existing model instances.
- `can_delete`: Permission to delete model instances.

## Groups and Permissions
- **Editors**: Can create and edit model instances (`can_create`, `can_edit`).
- **Viewers**: Can only view model instances (`can_view`).
- **Admins**: Have all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Setting Up Permissions
1. Add the custom permissions in the `Book` model's `Meta` class.
2. Create groups and assign relevant permissions in the Django admin panel.
3. Enforce permissions in views using the `@permission_required` decorator.

## Testing
- Users are assigned to groups (Editors, Viewers, Admins).
- Log in as different users to ensure that permissions are being enforced correctly in the views.
