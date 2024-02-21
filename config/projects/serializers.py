from rest_framework import serializers
from .models import Projects



class ProjectsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Projects.

    Поля:
    - id: Уникальный идентификатор.
    - link: Ссылки
    - image: Изображение.
    - description: Описание.
    """
    
    class Meta:
        model = Projects
        fields = '__all__'