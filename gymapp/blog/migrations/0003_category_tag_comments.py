# Generated by Django 5.1 on 2024-08-18 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blog_category_remove_comments_blog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان لاتین')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان لاتین')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بروزرسانی')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('email', models.EmailField(max_length=254, verbose_name='ادرس الکترونیکی')),
                ('messege', models.TextField(verbose_name='متن نظر')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog', verbose_name='مقاله')),
            ],
        ),
    ]
