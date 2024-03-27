from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Links(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    shortlink = models.CharField(max_length=100, verbose_name='Короткая ссылка')
    link = models.CharField(max_length=250, verbose_name='Полная ссылка')
    user = models.IntegerField(verbose_name='Код пользователя')

    class Meta:
        verbose_name='Ссылка'
        verbose_name_plural='Ссылки'

    def get_absolute_url(self):
        # return reverse_lazy('view_news', kwargs={'news_id': self.pk})
        # return reverse_lazy('home', kwargs={'pk': self.pk})
        return reverse_lazy('user_links', kwargs={'user': self.user})