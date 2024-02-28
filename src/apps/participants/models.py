from django.db import models



class ApplicationsForParticipants(models.Model):
    """Модель заявок участников.

    ### Attrs:
    - name (str):
        -Имя участника.
    - email (email):
        -Почта участника.
    - phone_number (int):
        - Номер телефона участника.
    - description (text):
        - Описание участника.
    """
    
    name = models.CharField(
        max_length=100, 
        verbose_name='ФИО'
    )
    
    email = models.EmailField(
        max_length=200, 
        verbose_name="Почта"
    )
    
    phone_number = models.IntegerField(
        verbose_name='Номер телефона', 
        help_text="Введите телефон клиента в формате: +996xxxxxxxxx"
    )
    
    description = models.TextField(
        verbose_name='Описание'
    )
    
    
    def __str__(self):
        return self.name