# Generated by Django 4.1.1 on 2023-10-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_remove_curso_cupo_asignacionalumnocurso_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacionalumnocurso',
            name='nota',
            field=models.FloatField(default=0.0),
        ),
    ]
