from rest_framework.permissions import BasePermission, SAFE_METHODS

class AdminRolePermission(BasePermission):
    message = 'Debes tener cuenta admin para acceder'
    def has_permission(self, request, view):
        print(request.user.username)
        if request.user.user_type == 1:
            return False
        return True


class EmprendeRolePremission(BasePermission):
    message = "Debe tener cuenta Emprendedor para acceder"    # El mensaje aquí indica un mensaje de error si no se pasa el permiso
    def has_permission(self,request,view):
        if request.user.user_type == 2:
                         # Falso significa que no hay permiso, información de mensaje rápida
                         # Verdadero es permiso para continuar la ejecución
            return False # Si el valor de user_type es siempre igual a2  , Significa que no se pasa el permiso y se emite el mensaje de solicitud de mensaje
        return True


class UserBasicRolePremission(BasePermission):
    message = "Debe tener cuenta basica para acceder"
    def has_permission(self,request,view):
        print(request.user.username)
        if request.user_type == 3:
            return False
        return True



# LA CLASE RECIBE EL OBJETO Y COMPRUEBA SI EL METODO ES POST, PUT O DELETE
class IsOwner(BasePermission):
    message = "No es propietario"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.id == obj.usuario


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

class IsUserOrReadOnly(BasePermission):
    """
      Custom permission to only allow owners of an object to edit it.
      """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.

        return obj.id == request.user


from rest_framework.authentication import SessionAuthentication

class UnsafeSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, *args, **kwargs):
        '''
        Bypass the CSRF checks altogether
        '''
        pass


