from django.db import models


class MainModel(models.Model):
    class Meta:
        db_table = 'main'

    base = models.TextField()
    short = models.TextField()
    clicks = models.PositiveIntegerField(default=0)
