from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):


    def has_permission(self, request, view):
        return request.user.is_staff or request.user == view.get_object().owner


