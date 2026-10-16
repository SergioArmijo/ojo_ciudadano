from django.test import TestCase

from .models import Role, User


class UserModelTests(TestCase):
    """Pruebas de humo para el modelo de usuario de la Etapa 1."""

    def test_crear_usuario_asigna_rol_ciudadano_por_defecto(self):
        user = User.objects.create_user(username="vecina1", password="clave-segura-123")
        self.assertEqual(user.role, Role.CIUDADANO)
        self.assertTrue(user.is_account_active)
        self.assertTrue(user.check_password("clave-segura-123"))

    def test_se_puede_crear_usuario_con_otro_rol(self):
        user = User.objects.create_user(
            username="operador1", password="clave-segura-123", role=Role.OPERADOR
        )
        self.assertEqual(user.role, Role.OPERADOR)
