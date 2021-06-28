import graphene


import prices_app.schema

# import graphql_jwt


class Query(prices_app.schema.Query, graphene.ObjectType):
    pass


# class Mutation(main.users.schema.Mutation,main.schema.Mutation, graphene.ObjectType):
#     token_auth = graphql_jwt.ObtainJSONWebToken.Field()
#     verify_token = graphql_jwt.Verify.Field()
#     refresh_token = graphql_jwt.Refresh.Field()


# schema = graphene.Schema(query=Query, mutation=Mutation)

schema = graphene.Schema(query=Query)