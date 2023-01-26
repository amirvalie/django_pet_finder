from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User=get_user_model()

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

def _is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return False

        
def _has_group_permission(user, required_groups):
    if user.is_anonymous:
        return False
    return False if False in [_is_in_group(user, group_name) for group_name in required_groups] else True

class IsSuperUserOrAuthorOrReadOnly(permissions.BasePermission):
    required_groups=['is_creator']
    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return bool(
            request.method in SAFE_METHODS or 
            (request.user.is_staff and has_group_permission) or 
            request.user.is_superuser
        )
    

