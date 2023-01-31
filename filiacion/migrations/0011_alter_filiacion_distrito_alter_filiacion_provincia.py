# Generated by Django 4.1.5 on 2023-01-30 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("filiacion", "0010_alter_filiacion_req_formato_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filiacion",
            name="distrito",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="filiacion.distrito",
            ),
        ),
        migrations.AlterField(
            model_name="filiacion",
            name="provincia",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="filiacion.provincia",
            ),
        ),
    ]
