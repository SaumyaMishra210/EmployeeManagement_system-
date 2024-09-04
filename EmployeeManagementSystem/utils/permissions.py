from django.core.exceptions import PermissionDenied

def is_authenticated(user):
    return user.is_authenticated

def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

def is_superuser(user):
    return user.is_superuser

def has_permission(user, permission_name):
    return user.has_perm(permission_name)

def check_group_and_superuser(user, group_name):
    if not is_authenticated(user):
        raise PermissionDenied("User is not authenticated")
    if not is_in_group(user, group_name) and not is_superuser(user):
        raise PermissionDenied("User does not have the required group or superuser status")
    return True
