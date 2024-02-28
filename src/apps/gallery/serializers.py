from rest_framework import serializers
from .models import Gallery



class GallerySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Gallery.

    Поля:
    - id: Уникальный идентификатор изображения.
    - created_at: Время публикации изображения.
    - image: Изображение.
    """
    class Meta:
        model = Gallery
        fields = '__all__'