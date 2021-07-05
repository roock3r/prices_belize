# Generated by Django 3.2.4 on 2021-07-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='prices-default-image.png', null=True, upload_to='product-images'),
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('article', models.ManyToManyField(to='prices_app.Article')),
            ],
        ),
    ]
