# Generated by Django 5.1 on 2024-08-18 13:50

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', models.CharField(max_length=100, verbose_name='توضیحات')),
                ('content', models.TextField(verbose_name='متن')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='تصویر')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.category', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='blogs', to='blog.tag', verbose_name='تگ ها')),
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