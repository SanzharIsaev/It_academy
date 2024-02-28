from rest_framework import viewsets
from .models import Comments
from .serializers import CommentsSerializer
from config.permissions import IsAdminOrReadOnly



class CommentsAPIView(viewsets.ModelViewSet):
    """Представление для работы с отзывами.

    Атрибуты:
    - queryset: Набор данных, из которого будут извлекаться данные об отзыве.
    - serializer_class: Сериализатор, используемый для преобразования отзывов в JSON и обратно.

    """
    
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAdminOrReadOnly,)
