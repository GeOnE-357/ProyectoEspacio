from django.apps import AppConfig

class ControlConfig(AppConfig):
    name = 'control'
    db_table= 'control_logs'

    def ready(self):
        import control.signals