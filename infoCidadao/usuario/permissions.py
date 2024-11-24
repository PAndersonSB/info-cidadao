from rest_framework.permissions import BasePermission

class IsCidadao(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_cidadao()

class IsOutroTipo(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_outro_tipo()
