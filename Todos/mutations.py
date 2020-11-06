import graphene

from .types import TodoType
from .models import UserTodos


class CreateTodo(graphene.Mutation):
    id = graphene.Int()
    todo_msg = graphene.String()
    is_done = graphene.Boolean()

    class Arguments:
        todo_msg = graphene.String()
        is_done = graphene.Boolean()

    def mutate(self, info, todo_msg, is_done):
        new_todo = UserTodos(todo_msg=todo_msg, is_done=is_done)
        new_todo.save()

        return CreateTodo(id=new_todo.id, todo_msg=new_todo.todo_msg, is_done=new_todo.is_done)


class UpdateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        id = graphene.Int()
        todo_msg = graphene.String(required=False)
        is_done = graphene.Boolean()

    def mutate(self, info, **kwargs):
        updating_todo = UserTodos.objects.get(id=kwargs.get('id'))
        updating_todo.todo_msg = kwargs.get('todo_msg', None)
        updating_todo.is_done = kwargs.get('is_done', None)
        updating_todo.save()

        return UpdateTodo(todo=updating_todo)


class DeleteTodo(graphene.Mutation):
    is_deleted = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        deleting_todo = UserTodos.objects.get(id=id)
        deleting_todo.delete()

        return DeleteTodo(is_deleted=True)
