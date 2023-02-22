from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

class JoinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'join'
