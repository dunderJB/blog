# Generated by Django 3.1.4 on 2020-12-14 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20201213_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_comentario', models.CharField(max_length=150)),
                ('email_comentario', models.EmailField(max_length=254)),
                ('comentario', models.TextField()),
                ('data_comentario', models.DateTimeField(default=django.utils.timezone.now)),
                ('publicado_cometario', models.BooleanField(default=False)),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('usuario_comentario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
