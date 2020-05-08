# Generated by Django 3.0.3 on 2020-05-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='视频id')),
                ('title', models.CharField(blank=True, max_length=512, null=True, verbose_name='标题')),
                ('category', models.CharField(blank=True, max_length=56, null=True, verbose_name='类型')),
                ('url', models.URLField(blank=True, max_length=256, null=True, verbose_name='播放地址')),
                ('gif_url', models.URLField(blank=True, max_length=512, null=True, verbose_name='图片地址')),
                ('created_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, db_index=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
                'ordering': ('-created_time', '-updated_time'),
            },
        ),
    ]