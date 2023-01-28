from rest_framework.permissions import BasePermission

ALLOWED_METHODS = ('GET','POST','PUT','HEAD', 'OPTIONS')

class IsSuperUserOrOwner(BasePermission):
    def has_permission(self,request,view):
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_superuser
        return bool(
            (request.method in ALLOWED_METHODS and request.user and request.user.is_authenticated) or
            (request.user.is_superuser)
        )
    def has_object_permission(self,request,view,obj):
        return bool(obj.user == request.user or request.user.is_superuser)