from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to="photos",  verbose_name="Фото")
    description = models.CharField(max_length=30, blank=True, verbose_name="Заголовок (не более 30 символов)")
    content=models.TextField(max_length=500, blank=True, verbose_name="Описание (не более 500 символов)")
    def __str__(self):
        return self.description
