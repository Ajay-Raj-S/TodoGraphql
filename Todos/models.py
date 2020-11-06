from django.db import models

# Create your models here.
class UserTodos(models.Model):
    todo_msg = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.todo_msg} | {self.is_done}'
