from django import forms
from .models import Comments


class CommentsForms(forms.ModelForm):
    """Формы для отзывов
    Поля:
    - name: Имя того, кто оставляет отзыв.
    - comment: Отзыв.
    """
    class Meta:
        model = Comments
        fields = '__all__'