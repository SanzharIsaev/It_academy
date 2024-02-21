from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comments.

    Поля:
    - id: Уникальный идентификатор отзыва.
    - name: Имя того, кто оставляет отзыв.
    - comment: Отзыв.
    """
    class Meta:
        model = Comments
        fields = '__all__'