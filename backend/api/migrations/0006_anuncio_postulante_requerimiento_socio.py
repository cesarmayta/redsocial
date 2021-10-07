# Generated by Django 3.2.8 on 2021-10-07 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_publicacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='titular', to='api.empresa')),
                ('estado', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='api.estado')),
                ('socio', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='socio', to='api.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='publicaciones')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='empresaSolicitante', to='api.empresa')),
                ('estado', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='api.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('mensaje', models.TextField()),
                ('estado', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='api.estado')),
                ('postulante', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='postulante', to='api.empresa')),
                ('requerimiento', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.requerimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='publicaciones')),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='anunciante', to='api.empresa')),
                ('estado', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='api.estado')),
            ],
        ),
    ]