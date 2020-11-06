from graphene_django.types import DjangoObjectType

from .models import UserTodos


class TodoType(DjangoObjectType):
    class Meta:
        model = UserTodos
