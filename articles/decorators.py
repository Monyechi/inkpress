from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from functools import wraps

def admin_required(function=None):
    @wraps(function)
    def _wrapped_view(request, *args, **kwargs):
        try:
            if not request.user.is_authenticated:
                return redirect('/login/')
            if not request.user.is_superuser:
                raise PermissionDenied("You do not have permission to access this page.")
            return function(request, *args, **kwargs)
        except PermissionDenied as e:
            # Log the error or handle it as needed
            print(f"PermissionDenied: {e}")
            raise
        except Exception as e:
            # Log unexpected errors
            print(f"Unexpected error: {e}")
            raise
    return _wrapped_view if function else _wrapped_view
