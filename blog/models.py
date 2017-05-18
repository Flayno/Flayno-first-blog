from django.db import models
from django.utils import timezone

#Определение модели
class Post(models.Model): # Post - имя модоли models.Model - обозначает что Post - это модель Django
    
    author = models.ForeignKey('auth.User')   # Свойство Автор             ForeignKey - ссылка на другую модель
    
    title = models.CharField(max_length=200)  # Свойство тайтл(заголовок)  CharField - текстовое поле                                       
                                                                        #  с ограничением на количество
                                                                        #  cимволов.
            
    text = models.TextField()                 # Свойство текст             TextField - текстовое поле
                                                                        #  для неограниченного длинного текста
        
    created_date = models.DateTimeField(      # Свойство дата создания     DateTimeField - дата и время
            default=timezone.now)             # Свойство 
    published_date = models.DateTimeField(    # Свойство дата публицации
            blank=True, null=True)            # Свойство

    def publish(self):                        # Метод для публикации записи publish - название
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
