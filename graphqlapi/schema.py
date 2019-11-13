import graphene
import graphql_jwt
from django.contrib.auth.models import User
from graphql_jwt.decorators import login_required

from graphqlapi.types import ProfileType, UserType
from seguridad.models import Profile
from .types import Query as SchemeQuery
from .mutation import Mutation as SchemeMutation


class Query(SchemeQuery, graphene.ObjectType):
    pass


class Mutation(SchemeMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
