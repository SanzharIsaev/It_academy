from rest_framework import serializers
from .models import AboutUs




class AboutUsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели AboutUs.

    Поля:
    - id: Уникальный идентификатор.
    - image: Изображение.
    - description: Описание.
    """
    class Meta:
        model = AboutUs
        fields = '__all__'