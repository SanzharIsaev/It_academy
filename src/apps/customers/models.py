from django.db import models


class ApplicationsForCustomers(models.Model):
    """Модель заявок заказчика.

    ### Attrs:
    - name (str):
        -Имя заказчика.
    - email (email):
        -Почта заказчика.
    - phone_number (int):
        - Номер телефона заказчика.
    - company (str):
        - Компания.
    - description (text):
        - Описание заказчика.
    
    """
    
    name = models.CharField(
        max_length=100, 
        verbose_name='ФИО'
    )
    
    email = models.EmailField(
        max_length=200, 
        verbose_name="Email"
    )
    
    phone_number = models.IntegerField(
        verbose_name='Номер телефона',
        help_text="Введите телефон клиента в формате: +996xxxxxxxxx"
    )
    
    company = models.CharField(
        max_length=200, 
        verbose_name='Компания'
    )
    
    description = models.TextField(
        verbose_name='Описание'
    )
    
    
    
    def __str__(self):
        return self.name