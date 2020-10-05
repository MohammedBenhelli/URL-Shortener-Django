import graphene
import short.schema

class Query(short.schema.Query, graphene.ObjectType):
    pass

class Mutation(short.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)