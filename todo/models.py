from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    name = models.CharField('名前', max_length=50)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作成者', on_delete=models.CASCADE)

    class Meta:
        db_table = 'todos'

    def __str__(self):
        return self.name