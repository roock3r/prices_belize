import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q


from .models import Article, ArticlePrice


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class ArticlePriceType(DjangoObjectType):
    class Meta:
        model = ArticlePrice


class Query(graphene.ObjectType):
    articles = graphene.List(ArticleType, search=graphene.String())
    article_prices = graphene.List(ArticlePriceType)

    def resolve_articles(self, info, search=None):
        if search:
            filter = (
                Q(name__icontains=search)|
                Q(description__icontains=search)
            )
            return Article.objects.filter(filter)
        return Article.objects.all()

    def resolve_article_prices(self, info):
        return ArticlePrice.objects.all()