"""
    schema.py contains base schema for the query and mutations
"""

import graphene

from .models import UserTodos
from .types import TodoType
from .mutations import CreateTodo, UpdateTodo, DeleteTodo


class Query(graphene.ObjectType):
    """
        Queries from the Todos app
    """
    todos = graphene.List(TodoType)

    def resolve_todos(self, info, **kwargs):
        return UserTodos.objects.all()


class Mutation(graphene.ObjectType):
    """
        Mutations from the Todo app
    """
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()


# Register the query and mutation on the root schema
schema = graphene.Schema(query=Query, mutation=Mutation)
