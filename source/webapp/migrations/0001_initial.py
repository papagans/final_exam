# Generated by Django 2.2 on 2020-03-14 04:48

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
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Подпись')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads', verbose_name='Файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('counter', models.BigIntegerField(default=0, verbose_name='Счетчик')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announce_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ['-created_at'],
            },
        ),
    ]
