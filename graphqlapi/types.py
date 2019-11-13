import graphene
from django.contrib.auth.models import User
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required

from seguridad.models import Profile
from main_app.models import Tree, Company, Opinion


class TreeType(DjangoObjectType):
    class Meta:
        model = Tree

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'profile',
            'groups',
            'user_permissions'
        )
class OpinionType(DjangoObjectType):
    class Meta:
        model = Opinion


class Query(object):
    tree = graphene.Field(TreeType, id=graphene.ID(required=True), name=graphene.String())
    all_trees = graphene.List(TreeType)
    all_public_trees = graphene.List(TreeType)
    meprofile = graphene.Field(ProfileType)
    me = graphene.Field(UserType)

    def resolve_all_trees(self, info, **kwargs):
        return Tree.objects.all()

    def resolve_all_public_trees(self, info, **kwargs):
        return Tree.objects.filter(show_in_home=True)

    def resolve_tree(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Tree.objects.get(pk=id)
        if name is not None:
            return Tree.objects.get(name=name)
        return None

    @login_required
    def resolve_meprofile(self, info):
        # Querying a single question
        return Profile.objects.get(user_id=info.context.user.id)

    @login_required
    def resolve_me(self, info):
        # Querying a single question
        return User.objects.get(pk=info.context.user.id)
