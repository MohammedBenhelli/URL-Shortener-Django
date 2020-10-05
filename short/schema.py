import graphene
from graphene_django import DjangoObjectType
from .models import URL
from django.db.models import Q

class URLType(DjangoObjectType):
    class Meta:
        model = URL

class Query(graphene.ObjectType):
    urls = graphene.List(URLType, url=graphene.String(), first=graphene.Int(), skip=graphene.Int())

    def resolve_urls(self, info, url=None, first=None, skip=None, **kwargs):
        query = URL.objects.all()
        print(query)
        if url:
            _filter = Q(url__icontains=url)
            query = query.filter(_filter)
        if first:
            query = query[:first]
        if skip:
            query = query[:skip]
        return query

class CreateURL(graphene.Mutation):
    url = graphene.Field(URLType)

    class Arguments:
        furl = graphene.String()

    def mutate(self, info, furl):
        url = URL(url=furl)
        url.save()
        return CreateURL(url=url)

class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()