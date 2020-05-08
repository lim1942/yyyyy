from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.


class Video(models.Model):

    id = models.CharField(primary_key=True,max_length=32,verbose_name='视频id')
    title =  models.CharField(max_length=512,verbose_name='标题', null=True, blank=True)
    category = models.CharField(max_length=56,verbose_name='类型', null=True, blank=True)
    url = models.URLField(max_length=256,verbose_name='播放地址', null=True, blank=True)
    gif_url = models.URLField(max_length=512,verbose_name='图片地址', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', db_index=True)
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', db_index=True)

    class Meta:
        ordering = (
            '-created_time',
            '-updated_time',
        )
        verbose_name_plural = verbose_name = '视频'

    def __str__(self):
        return self.title
