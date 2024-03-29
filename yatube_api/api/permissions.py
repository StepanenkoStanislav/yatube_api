from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Только автор может редактировать это.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == obj.author:
            return True
