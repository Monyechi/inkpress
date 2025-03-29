from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from functools import wraps

def admin_required(function=None):
    @wraps(function)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/')
        if not request.user.is_superuser:
            raise PermissionDenied("You do not have permission to access this page.")
        return function(request, *args, **kwargs)
    return _wrapped_view if function else _wrapped_view
