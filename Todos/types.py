"""
    types.py contains the Types for the schema from Django models
"""

from graphene_django.types import DjangoObjectType

from .models import UserTodos


class TodoType(DjangoObjectType):
    """
        TodoType models UserTodos
    """
    class Meta:
        model = UserTodos
