from rest_framework import serializers
from .models import ApplicationsForParticipants

class ApplicationForParticipantsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ApplicationForParticipants.

    Поля:
    - id: Уникальный идентификатор заявки.
    - name: Имя участника.
    - email: Почта участника.
    - description: Описание участника.
    - phone_number: Номер телефона участника.
    """
    class Meta:
        model = ApplicationsForParticipants
        fields = '__all__'







