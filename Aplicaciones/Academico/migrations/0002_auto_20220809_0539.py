# Generated by Django 2.2.3 on 2022-08-09 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido_paterno', models.CharField(max_length=20, verbose_name='Apellido paterno')),
                ('apellido_materno', models.CharField(max_length=20, verbose_name='Apellido materno')),
                ('nombres', models.CharField(max_length=20, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
                'db_table': 'docente',
                'ordering': ['apellido_paterno', '-apellido_materno'],
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='docente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Academico.Docente'),
        ),
    ]
