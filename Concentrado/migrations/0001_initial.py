# Generated by Django 5.0.7 on 2024-08-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad', models.IntegerField()),
                ('nombreEntidad', models.CharField(max_length=255)),
                ('distrito', models.IntegerField()),
                ('numeroDesignados', models.IntegerField()),
                ('numeroInscritos', models.IntegerField()),
                ('inscritosDesignados', models.DecimalField(decimal_places=2, max_digits=5)),
                ('conIngreso', models.IntegerField()),
                ('conIngresoInscritos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sinIngreso', models.IntegerField()),
                ('sinIngresoInscritos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('concluyeron', models.IntegerField()),
                ('concluyeronDesignados', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('numero', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('nombreEntidad', models.CharField(max_length=255)),
                ('numeroDeDistritos', models.IntegerField()),
                ('Logo', models.FileField(upload_to='documentos/')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroEntidad', models.IntegerField()),
                ('nivelEsperado', models.IntegerField()),
                ('nivelOptenido', models.IntegerField()),
            ],
        ),
    ]
