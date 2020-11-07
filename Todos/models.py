from django.db import models


class UserTodos(models.Model):
    """
        Basic todo model
    """
    todo_msg = models.CharField(max_length=256)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.todo_msg} | {self.is_done}'
