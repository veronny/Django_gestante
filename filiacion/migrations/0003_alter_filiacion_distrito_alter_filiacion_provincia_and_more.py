# Generated by Django 4.1.5 on 2023-01-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0002_provincia_red_microred_establecimiento_distrito"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filiacion",
            name="distrito",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="provincia",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="tipo_municipalidad",
            field=models.CharField(
                blank=True,
                choices=[(1, "Provincial"), (2, "Distrital")],
                max_length=100,
                null=True,
            ),
        ),
    ]
