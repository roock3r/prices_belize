import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from django.db.models import Q

from .models import Article, ArticlePrice, ArticleCategory


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class ArticlePriceType(DjangoObjectType):
    class Meta:
        model = ArticlePrice


class ArticleCategoryType(DjangoObjectType):
    class Meta:
        model = ArticleCategory


class Query(graphene.ObjectType):
    article = graphene.Field(ArticleType, id=graphene.String())
    articles = graphene.List(ArticleType, search=graphene.String())
    article_group = graphene.Field(ArticleCategoryType, id=graphene.String())
    article_groups = graphene.List(ArticleCategoryType)
    article_prices = graphene.List(ArticlePriceType)

    def resolve_article(self, info, id):
        return Article.objects.get(id=id)

    def resolve_article_prices(self, info):
        return ArticlePrice.objects.all()

    def resolve_article_group(self, info, id=None):
        if id:
            return ArticleCategory.objects.get(id=id)

    def resolve_article_groups(self, info):
        return ArticleCategory.objects.all()

    def resolve_articles(self, info, search=None):
        if search:
            filter = (
                    Q(name__icontains=search) |
                    Q(description__icontains=search)
            )
            return Article.objects.filter(filter)
        return Article.objects.all()
