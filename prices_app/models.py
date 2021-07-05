from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager
)
import logging

# Create your models here.

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("the given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Article(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="product-images", null=True, default="prices-default-image.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.slug,


class ArticlePrice(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pub_date = models.DateField()

    def __str__(self):
        return f'{self.article.name}-{self.pub_date}'


class ArticleCategory(models.Model):
    category = models.CharField(max_length=32)
    article = models.ManyToManyField(Article)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.category}-{self.updated_at}'
