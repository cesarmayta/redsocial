# Generated by Django 3.2.8 on 2021-10-07 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211006_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='publicaciones')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='empresaPublicante', to='api.empresa')),
                ('estado', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='api.estado')),
            ],
        ),
    ]
