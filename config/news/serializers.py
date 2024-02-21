from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели News.

    Поля:
    - id: Уникальный идентификатор новости.
    - time: Время публикации новости.
    - image: Изображение.
    - description: Описание.
    """
    class Meta:
        model = News
        fields = '__all__'