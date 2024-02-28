from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from config.permissions import IsAdminOrReadOnly



class NewsAPIView(viewsets.ModelViewSet):
    """Представление для работы с новостями.

    Атрибуты:
    - queryset: Набор данных, из которого будут извлекаться данные новости.
    - serializer_class: Сериализатор, используемый для преобразования заявок в JSON и обратно.

    """
    
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)