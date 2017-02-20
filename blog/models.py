from django.db import models


# Create your models here.
class Article(models.Model):
    """表示文章的模型"""

    # 标题
    title = models.CharField(max_length=100)

    # 文章的类别 blank是数据验证范畴
    category = models.CharField(max_length=50, blank=True)

    # 文章的发布时间
    date_time = models.DateTimeField(auto_now_add=True)

    # 文章的主体内容
    content = models.TextField(blank=True, null=True)

    # 返回Model的描述
    def __str__(self):
        return self.content[:100]

    # 元信息
    class Meta:
        ordering = ['-date_time']
