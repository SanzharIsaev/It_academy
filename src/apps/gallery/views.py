from django.shortcuts import render
from rest_framework import viewsets
from .models import Gallery
from .serializers import GallerySerializer
from config.permissions import IsAdminOrReadOnly



class GalleryAPIViews(viewsets.ModelViewSet):
    """ Представление для работы с галереей.

    Атрибуты:
    - queryset: Набор данных, из которого будут извлекаться данные о галерее.
    - serializer_class: Сериализатор, используемый для преобразования галереи в JSON и обратно.

    """
    
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = (IsAdminOrReadOnly,)