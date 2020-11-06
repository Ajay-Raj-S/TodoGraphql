import graphene

import Todos.schema


class Query(Todos.schema.Query, graphene.ObjectType):
    pass


class Mutation(Todos.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
