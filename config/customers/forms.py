from django import forms
from .models import ApplicationsForCustomers


class ApplicationsForCustomersForms(forms.ModelForm):
    """Формы для заявок заказчиков
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