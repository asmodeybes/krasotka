from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _





class Letter (models.Model):
    name = models.CharField(max_length=30, verbose_name= "Имя пользователя")
    email = models.EmailField(verbose_name=_("Email"), blank=True,)
    subject=models.CharField(max_length=30, verbose_name= "Тема", blank=True)
    message = models.TextField(max_length=500, verbose_name= "Сообщение", blank=True)
    published_date = models.DateTimeField(auto_created=True, verbose_name=_("Дата отправки"))


    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _("Сообщение")
        verbose_name_plural = _("Сообщения")


