from django.conf import settings
from django.shortcuts import redirect
from django.utils.http import url_has_allowed_host_and_scheme
from urllib.parse import urlencode


class ForceLogoutOnServerRestartMiddleware:
    """
    If the server restarts/reloads, settings.SERVER_RUN_NONCE changes.
    We stamp the session with the current nonce: if it doesn't match later,
    we flush the session to force re-login.
    """
    
    SESSION_KEY = "_server_run_nonce"
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Only enforce for authenticated sessions
        if getattr(request, "user", None) and request.user.is_authenticated:
            current = getattr(settings, "SERVER_RUN_NONCE", None)
            stored = request.session.get(self.SESSION_KEY)
            
            # First request after login (or first time we see session) -> stamp it
            if stored is None:
                request.session[self.SESSION_KEY] = current
                
            # Server restarted/reloaded -> nonce changed -> force logout
            elif stored != current:
                request.session.flush()
                
                # Redirect to login with ?next=<original path>
                next_url = request.get_full_path()
                login_url = settings.LOGIN_URL
                
                # Safety check for next= parameter
                if url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    query = urlencode({"next": next_url})
                    return redirect(f"{login_url}?{query}")
                    
                return redirect(login_url)
                
        return self.get_response(request)
