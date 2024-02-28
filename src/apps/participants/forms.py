from django import forms
from .models import ApplicationsForParticipants


class ApplicationsForParticipantsForms(forms.ModelForm):
    """Формы для заявок участников
    Поля:
    - id: Уникальный идентификатор заявки.
    - name: Имя участника.
    - email: Почта участника.
    - description: Описание участника.
    - phone_number: Номер телефона участника.
    """
    class Meta:
        model = ApplicationsForParticipants
        fields = '__all__'