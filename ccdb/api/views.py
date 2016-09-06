from django.contrib.auth import user_logged_in

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from djoser.views import (LoginView, PasswordResetView,
                          PasswordResetConfirmView)


class Login(LoginView):
    def action(self, serializer):
        user = serializer.user
        token, _ = Token.objects.get_or_create(user=user)
        user_logged_in.send(sender=user.__class__,
                            request=self.request,
                            user=user)
        return Response(
            data={'token': token.key, 'id': token.user_id},
            status=status.HTTP_200_OK,
        )


class PasswordReset(PasswordResetView):
    """Overriding to return empty object, for ember-ajax"""
    def action(self, serializer):
        response = super(PasswordReset, self).action(serializer)
        response.data = {}
        return response


class PasswordResetConfirm(PasswordResetConfirmView):
    """Overriding to return empty object, for ember-ajax"""
    def action(self, serializer):
        response = super(PasswordResetConfirm, self).action(serializer)
        response.data = {}
        return response
