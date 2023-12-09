from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    short_desc = models.CharField(max_length=250)
    body = models.TextField()

    # class Meta:
    #     db_table = 'post'

    def __str__(self) -> str:
        return self.title
