from rest_framework import serializers
from .models import ApplicationsForCustomers

class ApplicationForCustomersSerializer(serializers.ModelSerializer):
    """Сериализатор для модели ApplicationForCustomers.

    Поля:
    - id: Уникальный идентификатор заявки.
    - name: Имя заказчика.
    - email: Почта заказчика.
    - description: Описание заказчика.
    - phone_number: Номер телефона заказчика.
    - company: Компания заказчика.
    """
    class Meta:
        model = ApplicationsForCustomers
        fields = '__all__'