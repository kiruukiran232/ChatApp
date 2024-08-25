from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'registration'

    
class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
