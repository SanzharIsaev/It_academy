from django import forms
from .models import Team



class TeamForms(forms.ModelForm):
    """Формы для нашей команды

    Поля:
    - id: Уникальный идентификатор.
    - name(str) - имя участника
    - job_title(str) - должность
    - image(image) - изображение
    - description(text) - описание
    - linkedin(ссылки) - ссылки
    """
    class Meta:
        model = Team
        fields = '__all__'