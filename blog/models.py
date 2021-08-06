from django.db import models
from django.urls import reverse
class Post(models.Model):
    author = models.CharField(max_length=44,
                              null=True,
                              unique=False,)
    title = models.CharField(max_length=88,
                             help_text='Введите название',
                             null=False,
                             unique=True,
                             blank=True,
                             )
    content = models.TextField()
    datetime_add = models.DateTimeField(null=False,
                                        auto_now_add=True,
                                        db_index=True,
                                        )
    def __str__(self):
        return self.title

    def __dir__(self):
        return self.datetime_add

    def get_absolute_url(self):
        return reverse('detail_blog', args=[str(self.id)])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
