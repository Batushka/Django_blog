from django.db import models

# Create your models here.

'''
class PostApi(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User',
                              related_name='api_posts',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class CommentApi(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User',
                              related_name='api_comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey('PostApi',
                             related_name='api_comments',
                             on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class CategoryApi(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80, blank=True, default='')
    owner = models.ForeignKey('auth.User',
                              related_name='api_categories',
                              on_delete=models.CASCADE)
    posts = models.ManyToManyField('PostApi',
                                   related_name='api_categories')

    class Meta:
        ordering = ['created']
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

'''
