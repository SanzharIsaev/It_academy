from django.db import models

class Gallery(models.Model):
    """Модель для галереи

    Args:
    - image (image):
        - Изображение.
    - created_at (date):
        - Дата публикации.
        
    """
    
    image = models.ImageField(
        upload_to=('images/'), 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    
    created_at = models.DateField(
        auto_now=True
    )