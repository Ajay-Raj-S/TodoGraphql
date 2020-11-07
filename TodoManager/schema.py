"""
    Root schema inherits from multiple apps queries and mutations
"""

import graphene

import Todos.schema


class Query(Todos.schema.Query, graphene.ObjectType):
    """
        Inherits Query from all the apps
    """
    pass


class Mutation(Todos.schema.Mutation, graphene.ObjectType):
    """
        Inherits Mutations from all the apps
    """
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
