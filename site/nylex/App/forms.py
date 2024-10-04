from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm

class SecurityKeyAuthenticationForm(AdminAuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not hasattr(user, 'has_security_key') or not user.has_security_key():
            raise forms.ValidationError(
                "This account requires a security key.",
                code='no_security_key'
            )
