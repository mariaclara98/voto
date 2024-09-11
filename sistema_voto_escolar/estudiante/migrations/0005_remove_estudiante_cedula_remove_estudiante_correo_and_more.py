# Generated by Django 5.0.6 on 2024-07-10 00:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_alter_curso_nivel_alter_curso_paralelo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='cedula',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='nombre',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
