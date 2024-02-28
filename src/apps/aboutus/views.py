from rest_framework import viewsets
from .models import AboutUs
from .serializers import AboutUsSerializer
from config.permissions import IsAdminOrReadOnly


class AboutUsAPIView(viewsets.ModelViewSet):
    """Представление "О нас".

    Атрибуты:
    - queryset: Набор данных, из которого будут извлекаться данные о нас.
    - serializer_class: Сериализатор, используемый для преобразования в JSON и обратно.

    """
    
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = (IsAdminOrReadOnly,)
