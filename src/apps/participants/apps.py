from django.apps import AppConfig


class ParticipantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.participants'
    verbose_name = 'Участники'

    def ready(self) -> None:
        """
    Метод ready, который выполняется при загрузке приложения.

    В данном случае, происходит импорт модуля с обработчиками сигналов (views) для регистрации сигналов.
    Обработчики сигналов используются для выполнения определенных действий при определенных событиях, таких
    как сохранение экземпляра модели.

    Примечание:
    - Регистрация сигналов обычно выполняется в файле приложения (apps.py) в методе ready для удобства.
    - В данном случае, import происходит внутри метода ready, чтобы избежать циклических зависимостей
      при загрузке приложения.
    """
        import apps.participants.views

