from rest_framework import viewsets
from .models import ApplicationsForParticipants
from .serializers import ApplicationForParticipantsSerializer




class ApplicationsForParticipantsAPIView(viewsets.ModelViewSet):
    """Представление для работы с заявками участников.

    Атрибуты:
    - queryset: Набор данных, из которого будут извлекаться заявки участников.
    - serializer_class: Сериализатор, используемый для преобразования заявок в JSON и обратно.

    """
    
    queryset = ApplicationsForParticipants.objects.all()
    serializer_class = ApplicationForParticipantsSerializer
