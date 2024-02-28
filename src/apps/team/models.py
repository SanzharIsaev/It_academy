from django.db import models


class Team(models.Model):
    
    """
    
    Модель для нашей команды
    
    
    name(str) - имя участника
    job_title(str) - должность
    image(image) - изображение
    description(text) - описание
    linkedin(ссылки) - ссылки
    
    """
    
    name = models.CharField(
        max_length=100, 
        verbose_name='Имя'
    )
    
    job_title = models.CharField(
        max_length=50
    )
    
    image =models.ImageField(
        upload_to=('team_img/'), 
        height_field=None, 
        width_field=None, 
        max_length=None
    )
    
    description = models.TextField(
        verbose_name='О себе'
    )
    
    linkedin = models.CharField(
        max_length=1000
    )
    
    
    def __str__(self):
        return self.name