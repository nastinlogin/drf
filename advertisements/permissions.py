from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """Разрешение: изменять/удалять может только автор объекта."""

    def has_object_permission(self, request, view, obj):
        # Безопасные методы (GET, HEAD, OPTIONS) разрешены всем
        if request.method in SAFE_METHODS:
            return True
        # Изменять/удалять может только автор
        return obj.creator == request.user