from django.db import models

class News(models.Model):
    
    """Модель для новостей.

    ### Attrs:
    - time (DateTime):
        -Время создания новости.
    - image (image):
        -Изображение.
    - descriptiom (text):
        -Описание.
       
    """
    
    time = models.DateField(
        auto_now=True
    )
    
    image = models.ImageField(
        upload_to=None, 
        height_field=None, 
        width_field=None, 
    )
    
    decription = models.TextField(
        max_length=500, 
        verbose_name='Описание'
    )
    
    
    def __str__(self):
        return self.decription