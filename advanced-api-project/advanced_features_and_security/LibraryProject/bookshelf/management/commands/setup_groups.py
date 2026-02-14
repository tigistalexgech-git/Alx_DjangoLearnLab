# advanced_features_and_security/bookshelf/management/commands/setup_groups.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Article

class Command(BaseCommand):
    help = "Create groups and assign permissions"

    def handle(self, *args, **kwargs):
        # Create groups
        groups = ["Editors", "Viewers", "Admins"]
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            self.stdout.write(f"Group {group_name} {'created' if created else 'exists'}")

        # Assign permissions
        can_view = Permission.objects.get(codename="can_view")
        can_create = Permission.objects.get(codename="can_create")
        can_edit = Permission.objects.get(codename="can_edit")
        can_delete = Permission.objects.get(codename="can_delete")

        # Viewers: can view
        viewers = Group.objects.get(name="Viewers")
        viewers.permissions.set([can_view])
        viewers.save()

        # Editors: view + create + edit
        editors = Group.objects.get(name="Editors")
        editors.permissions.set([can_view, can_create, can_edit])
        editors.save()

        # Admins: all permissions
        admins = Group.objects.get(name="Admins")
        admins.permissions.set([can_view, can_create, can_edit, can_delete])
        admins.save()

        self.stdout.write(self.style.SUCCESS("Groups and permissions configured successfully!"))
