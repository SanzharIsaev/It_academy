from django.db import models



class Projects(models.Model):
    
    """
    Модель для проектов.

    ### Attrs:
    - image (image):
        -Изображение.
    - descriptiom (text):
        -Описание.
    - link (str):
        -Ссылки.
    
    
    """
    description = models.TextField(
        verbose_name='Описание'
    )
    
    link = models.CharField(
        max_length=1000
    )
    
    image = models.ImageField(
        upload_to=('projectsimg/'), 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    
    
    def __str__(self):
        return self.description
    
    