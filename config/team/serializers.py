from rest_framework import serializers
from .models import Team



class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Team.

    Поля:
    - id: Уникальный идентификатор.
    - name(str) - имя участника
    - job_title(str) - должность
    - image(image) - изображение
    - description(text) - описание
    - linkedin(ссылки) - ссылки
    """
    class Meta:
        model = Team
        fields = '__all__'