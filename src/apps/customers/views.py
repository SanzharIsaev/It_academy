from rest_framework import viewsets
from .models import ApplicationsForCustomers
from .serializers import ApplicationForCustomersSerializer




class ApplicationsForCustomersAPIView(viewsets.ModelViewSet):
    """Представление для работы с заявками заказчиков.

    Атрибуты:
    - queryset: Набор данных, из которого будут извлекаться заявки заказчиков.
    - serializer_class: Сериализатор, используемый для преобразования заявок в JSON и обратно.

    """
    
    queryset = ApplicationsForCustomers.objects.all()
    serializer_class = ApplicationForCustomersSerializer

