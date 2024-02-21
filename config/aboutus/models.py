from django.db import models


class AboutUs(models.Model):
    
    """
    Модель "О нас".

    ### Attrs:
    - image (image):
        -Изображение.
    - descriptiom (text):
        -Описание.
    
    
    """
    
    description = models.TextField(
        verbose_name='О нас'
    )
    
    image = models.ImageField(
        upload_to=('about_us_img/'), 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    
    def __str__(self):
        return self.text