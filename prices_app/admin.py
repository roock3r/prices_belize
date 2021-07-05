from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from . import models
# Register your models here.

admin.site.register(models.Article)
admin.site.register(models.ArticlePrice)
admin.site.register(models.ArticleCategory)