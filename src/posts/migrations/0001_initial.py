# Generated by Django 2.2.10 on 2021-10-15 11:24

from django.db import migrations, models
import djongo.models.fields
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('comments', djongo.models.fields.ArrayField(model_container=posts.models.Comment)),
            ],
        ),
    ]
