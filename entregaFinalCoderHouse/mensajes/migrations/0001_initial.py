# Generated by Django 3.2.9 on 2022-01-11 01:18

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
            name='Canal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanalUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateField(auto_now=True)),
                ('canal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mensajes.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CanalMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateField(auto_now=True)),
                ('texto', models.TextField()),
                ('canal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mensajes.canal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='canal',
            name='usuarios',
            field=models.ManyToManyField(blank=True, through='mensajes.CanalUsuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
