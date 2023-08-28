from rest_framework import permissions

# Permission to check the owner of a product
class IsProductOwner(permissions.BasePermission):
    message = 'Editing products is restricted to the seller only!'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.seller == request.user