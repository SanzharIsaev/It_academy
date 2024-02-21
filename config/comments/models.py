from django.db import models



class Comments(models.Model):
    
    """
    Модель отзывов.

    ### Attrs:
    - name (str):
        -Имя того, кто оставляет отзыв.
    - comment (text):
        -Отзыв.
    
    
    """
    
    name = models.CharField(max_length=150, verbose_name='Имя')
    comment = models.TextField(verbose_name='Отзыв')
    
    def __str__(self):
        return self.name
