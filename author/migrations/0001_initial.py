# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 09:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=30)),
                ('description', models.CharField(default="I'm a boring human with nothing to say about him/herself", max_length=1000)),
                ('profile_pic', models.FileField(default='author/static/author/img/profile_pics/no-image.jpg', upload_to='author/static/author/img/profile_pics/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]