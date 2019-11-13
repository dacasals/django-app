import graphene
from graphene_file_upload.scalars import Upload

from main_app.models import *
from .types import *


class CreateOpinionMutation(graphene.Mutation):
    class Input(object):
        tree = graphene.Int()
        name = graphene.String()
        rating = graphene.String()
        color = graphene.String()
        rotation = graphene.String()
        browser = graphene.String()
        platform = graphene.String()
        clientip = graphene.String()
        like_opinion = graphene.Int()
        not_like_opinion = graphene.Int()
        share_facebook = graphene.Int()
        share_twitter = graphene.Int()

    name = graphene.Field(OpinionType)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '')
        tree = kwargs.get('tree')
        color = kwargs.get('color', '')
        rotation = kwargs.get('rotation', '')
        browser = kwargs.get('browser', '')
        platform = kwargs.get('platform', '')
        clientip = kwargs.get('clientip', '')
        like_opinion = kwargs.get('like_opinion', 0)
        not_like_opinion = kwargs.get('not_like_opinion', 0)
        share_facebook = kwargs.get('share_facebook', 0)
        share_twitter = kwargs.get('share_twitter', 0)
        obj = Opinion.objects.create(
            name=name,
            color=color,
            rotation=rotation,
            browser=browser,
            platform=platform,
            clientip=clientip,
            like_opinion=like_opinion,
            not_like_opinion=not_like_opinion,
            share_facebook=share_facebook,
            share_twitter=share_twitter,
            tree_id=tree
        )
        return CreateOpinionMutation(name=obj)


class ProfileMutation(graphene.Mutation):
    class Input(object):
        company = graphene.String()
        name = graphene.String()
        last_name = graphene.String()
        zipcode = graphene.String()
        country = graphene.String()
        city = graphene.String()
        avatar = Upload(required=False)

    profile = graphene.Field(ProfileType)

    @staticmethod
    def mutate(root, info, **kwargs):
        # company = kwargs.get('company')
        name = kwargs.get('name')
        last_name = kwargs.get('last_name')
        zipcode = kwargs.get('zipcode')
        country = kwargs.get('country')
        city = kwargs.get('city')
        avatar = kwargs.get('avatar')

        profile = Profile.objects.get(user_id=info.context.user.id)
        # if company:
        #     profile.company = company
        if name:
            profile.name = name
        if last_name:
            profile.last_name = last_name
        if zipcode:
            profile.zipcode = zipcode
        if country:
            profile.country = country
        if city:
            profile.city = city
        if avatar:
            profile.avatar = avatar
        profile.save()
        return ProfileMutation(profile=profile)


class Mutation(graphene.AbstractType):
    create_opinion = CreateOpinionMutation.Field()
    update_profile = ProfileMutation.Field()
