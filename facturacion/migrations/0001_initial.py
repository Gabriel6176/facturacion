# Generated by Django 5.1.3 on 2024-11-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MesAno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("año", models.IntegerField()),
                (
                    "mes",
                    models.CharField(
                        choices=[
                            ("01", "Enero"),
                            ("02", "Febrero"),
                            ("03", "Marzo"),
                            ("04", "Abril"),
                            ("05", "Mayo"),
                            ("06", "Junio"),
                            ("07", "Julio"),
                            ("08", "Agosto"),
                            ("09", "Septiembre"),
                            ("10", "Octubre"),
                            ("11", "Noviembre"),
                            ("12", "Diciembre"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
            options={
                "ordering": ["año", "mes"],
                "unique_together": {("año", "mes")},
            },
        ),
    ]
