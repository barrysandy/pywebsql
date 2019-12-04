from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('标题', max_length=20)
    author = models.CharField('作者', max_length=20)
    content = models.TextField('内容')

    class Meta:
        verbose_name_plural = '文章'
        verbose_name = '文章'
        ordering = ['id']

class Host(models.Model):
    ip = models.CharField('ip地址', max_length=100)
    port = models.CharField('端口号', max_length=10)
    name = models.CharField('主机名', max_length=50)
    hostDesc = models.CharField('主机描述', max_length=200)

